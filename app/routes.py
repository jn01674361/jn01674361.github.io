from app import app
from flask import render_template, request
from app import rule_based_chatbot
import os

sent_tokens = 0
word_tokens = 0

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html')

@app.route('/leo')
def leo():
    global sent_tokens
    global word_tokens

    sent_tokens, word_tokens = rule_based_chatbot.preprocess(open('app/chili_pepper_madness.txt', 'r', errors='ignore'))

    return render_template('leo.html')

@app.route('/leo', methods=['POST'])
def submit_leo():
    global sent_tokens
    global word_tokens
    return render_template('leo.html', text = rule_based_chatbot.short_convo(request.form['text'], sent_tokens, word_tokens))
