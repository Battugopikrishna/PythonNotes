"""Hello everyone!
This is my personal Python Notes where I can use for my future refer and also to available every thing
 in One Place"""
"""
In the below code whatever having hashcode '#' you can remove that part of code and it will execute when you run
if you wish to run multipule line of code and you need remove lot of '/' then there is a tip to do in a single click
by selecting the required code just press 'cltr + / (in windows)' 'command + /(in MacOS)'
same if you don't want to run the code and want to comment it use  the same commands.
"""
# Python is high level programming language because this can be understood by users and the computer also
# And Programming language is a medium which helps us to communicate with system

"""
Python Literals

literals are nothing but numbers
Integers and Floats 
Integer = 1, 2, 3, 100, 1000, 0, -1, -2, -3, -100, -1000
Floats = 1.0, 2.23, 3.78, 100.00, 0.00, -1.0, -2.456, -1000.423
Below are the Examples
"""
# a = 10
# print(a)
# print(type(a))
# aa = 10.0
# print(aa)
# print(type(aa))

"""
Python Variable
The variable will reserve memory location.
example a = 10 that means we are assign the 10 to the variable 'a'
Note: Python is a case sensitive example: a = 10 and print(A) the output will be error and if you try print(a) then the output is 10.
"""

"""
If you want to comment in the python code 
For single line comment use - ‘#’
For the multiple line comment use - ‘ “ “ “ ‘ at the starting of the line and ‘ “ “ “ ‘ and at the ending of the comment line.
Python Datatype
Primitive Datatypes
-Integers
-Floats
-Strings
-Boolean
-None (spl datatype)
"""
# #Example for the Integer
# aage = 25
# print(aage)
# print(type(aage))
# #Example for the Float
# percentt = 89.90
# print(percentt)
# print(type(percentt))
# #Example for the String
# peru = 'GOPI'
# print(peru)
# print(type(peru))
# # here we have number spl char and space still this is string
# mix_peru = 'KGF part-3'
# print(mix_peru)
# print(type(mix_peru))
# #Example for Boolean
# bo = True # 'T' should be capital
# print(bo)
# print(type(bo))
#
# nobe = False # 'F' should be capital
# print(nobe)
# print(type(nobe))
# #Example for the spl data type None
# spl = None #'N' should be capital
# print(spl)
# print(type(spl))

"""
There are few Keyword which we are use them in the python and 
we can't use those keyword to assign any value
Example: 'break' is a keyword and we can't use it like 'break = 100' 
it will throw an error. so if want to know the keywords in python run the below code.
"""

# import keyword      #first we need to import the keyword in the code.
# print(keyword.kwlist)   #kwlist is a keyword to get all the list of keyword.

"""
Basic operations with the strings
now we are learning how many type we have to write a string and 
how to find the length of a string using 'len()'
how to join two strings.
"""

# s1 = "hello world" # using double quotes
# print(s1)
# print(type(s1))
#
# s2 = 'hello world' # using single quotes
# print(s2)
# print(type(s2))
#
# s3 = """hello world
# this is second line
# this is third line"""  # this is with triple quotes.
# print(s3)              # if the output print in single line and having '\n' then it represent has new line in the output.
# print(type(s3))

"""
Find the length of a string using 'len()'
and if you are using space in between the variable then it will also calculate and show in the length.
"""

# a1 = 'Gopi'
# print(len(a1))
# a2 = 'Gopi Krishna'
# print(len(a2))

"""
What is indexing in python ?
indexing is nothing but positioning of every letter in the string internal is called indexing.
and indexing count start with '0, 1, 2, 3, ....' not like '1, 2, 3, ....' 
because python always count zero first.
not only in python in every programming language count start with zero
because programming language uses binary code and binary code always start with zero.
Example: Gopi Battu
         0123456789
negative indexing is start with -1 and start position will be from last to first
Example:  G o p i
         -4-3-2-1          
indexing as use '[]' to get the desire result
"""
Name = 'Gopi'
print(Name[0]) # output will get 'G'
print(Name[-1]) #output will get 'i'
