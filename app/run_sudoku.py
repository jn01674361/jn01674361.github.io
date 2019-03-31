import os
home = os.getcwd()
os.chdir("sudoku/com/sudoku/build")
os.system("java -jar sudoku.jar")

#javapackager -deploy -outdir deployed -outfile outfile -width 500 -height 500 -name SudokuGUI -appclass com.sudoku.SudokuGUI -v -srcdir compiled
#javapackager -createjar -outdir compiled -outfile myapp -appclass application.Main -srcdir bin -v
