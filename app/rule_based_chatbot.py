import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer #convert a collection of raw documents to a matrix of TF-IDF features
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template

#RESPONSE IS THE FUNCTION THAT GENERATES ANSWERS TO QUESTIONS

# app=Flask(__name__)

# @app.route('/agent0')

def flaskTest():
    return "flaskTest"

def agent0():
    return render_template('agent0.html')  # render a template

def preprocess(f):

    # f = open(afile, 'r', errors = 'ignore')

# f = open('lalaland_script.txt', 'r', errors = 'ignore')
    raw= f.read()
    raw = raw.lower()
    nltk.download('punkt')
    nltk.download('wordnet')

    sent_tokens = nltk.sent_tokenize(raw) #converts raw text to list of sentences
    word_tokens = nltk.word_tokenize(raw) #converts raw text to list of words

    return sent_tokens, word_tokens


# STEMMING is the process of reducing inflected (or sometimes derived) 
# words to their stem, base or root form
#
# A slight variant of stemming is LEMMATIZATION. The major difference 
# between these is, that, stemming can often create non-existent words, 
# whereas lemmas are actual words. So, your root stem, meaning the word 
# you end up with, is not something you can just look up in a dictionary, 
# but you can look up a lemma
#
#



def LemTokens(tokens, lemmer=nltk.stem.WordNetLemmatizer()):
    lemmer = nltk.stem.WordNetLemmatizer() 
    return [lemmer.lemmatize(token) for token in tokens]



def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "hey", "yo"]

GREETING_RESPONSES = ["hi", "hey", "aloha", "shalom", "hola"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


#
# TFIDF = Term Frequency - Inverse Document Frequency
# 
# Term Frequency: is a scoring of the frequency of the word in 
# the current document.
# 
# TF = (Number of times term t appears in a document)/(Number of 
# terms in the document)
#
# Inverse Document Frequency: is a scoring of how rare the word 
# is across documents.
#
#IDF = 1+log(N/n), where, N is the number of documents and n is 
# the number of documents a term t has appeared in.


# Cosine similarity is a measure of similarity between two non-zero vectors. 
# Using this formula we can find out the similarity between any two documents 
# d1 and d2.
#
# Cosine Similarity (d1, d2) =  Dot product(d1, d2) / ||d1|| * ||d2||




def response(user_respone, sent_tokens):

    # We define a function response which searches the user?s utterance for one 
    # or more known keywords and returns one of several possible responses. If 
    # it doesn?t find the input matching any of the keywords, it returns a 
    # response:? I am sorry! I don?t understand you?
    #

    robo_response = ''

    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)

    # Cosine similarity will be used to find the similarity between words 
    # entered by the user and the words in the corpus. 
    #

    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response = robo_response + "What?"
    else:
        robo_response = robo_response + sent_tokens[idx]
    return robo_response



# @app.route('/main')
def start_bot(sent_tokens, word_tokens):
    
    flag = True
    print("CHAT WITH ME!")

    while(flag):
        user_response = input()
        user_response = user_response.lower()
        if(user_response!='bye'):
            if(user_response in ['thanks', 'thank you']):
                flag = False
                print(": You are welcome...")
            else:
                if(greeting(user_response)!=None):
                    print("LEONARDO: "+greeting(user_response))
                else:
                    sent_tokens.append(user_response)

                    word_tokens = word_tokens + nltk.word_tokenize(user_response)
                    final_words = list(set(word_tokens))
                    print("LEONARDO: ", end="")

                    #HERE IS WHERE THE MATCHING HAPPENS
                    print(response(user_response, sent_tokens))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            print("LEONARDO: Bye!")
            return

def short_convo(question, sent_tokens, word_tokens):
    question = question.lower()
    if(question!='bye'):
        if(question in ['thanks', 'thank you']):
            return "You are welcome..."
        else:
            if(greeting(question)!=None):
                return greeting(question) 
            else:
                sent_tokens.append(question)

                word_tokens = word_tokens + nltk.word_tokenize(question)
                final_words = list(set(word_tokens))

                #HERE IS WHERE THE MATCHING HAPPENS
                return response(question, sent_tokens)
    else:
        return "Bye!"

if __name__ == '__main__':
    sent_tokens, word_tokens = preprocess()
    start_bot(sent_tokens, word_tokens)





