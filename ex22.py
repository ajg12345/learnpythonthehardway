#what have a i learned so far:
"""
the following lines are pretty novel here:
from sys import argv

script, filename = argv
----
The way that 
file = open(filename)
file.readline()
simply reads the line as is until \n and if you print it, you'll also print the \n character
and that there is a file.truncate() function
and that the file = open(filename, 'w') will immeadiately truncate the file anyway
and that file.read() will return the contents of the file
---
that
formatstring =  f'this line will be print with {a} variable' 
statements are clear and handy
and there is 
othertype = 'this line will have 2 variables here{} and here{}'.format(1,2)
"""
othertype = 'this line will have 2 variables here{} and here{}'.format(1,2)
print(othertype)
a = 'soup'
formatstring =  f'this line will be print with {a} variable' 
print(formatstring)
"""
and finally that the *arg is a cheap and easy way to have many variables in a function definition
"""
