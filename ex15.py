from sys import argv
#uses the argv function in the sys module to get command line arguments to the script
script, filename = argv
#opens the file and returns a file handler
txt = open(filename)
#fprint statments and a filehandler read to print its contents
print(f"Here's your file {filename}:")
print(txt.read())
#collecting a string as input
print("Type the filename again:")
file_again = input("> ")
#using this string in order to open a file and file handler
txt_again = open(file_again)
#attempting to read that file handler
print(txt_again.read())
txt.close()
txt_again.close()