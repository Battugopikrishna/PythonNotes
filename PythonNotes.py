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

                              #######End of Variable#########
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

                        #######End of Basic operations with the strings########
"""
What is indexing in python ?
indexing is nothing but positioning of every letter in the string internal is called indexing.
and indexing count start with '0, 1, 2, 3, ....' not like '1, 2, 3, ....' 
because python always count zero first.
not only in python in every programming language count start with zero
because programming language uses binary code and binary code always start with zero.
Example: Gopi Battu
         0123456789 is called postive indexing count start from left to right
negative indexing is start with -1 and start position will be from right to left
Example:  G o p i
         -4-3-2-1          
indexing as use '[]' to get the desire result
"""
# Name = 'Gopi'
# print(Name[0]) # output will get 'G'
# print(Name[-1]) #output will get 'i'


                       ######End of indexing in python########
"""
Joining two string called Concatenation of strings by using '+' in the print
"""

# a1 = 'Hello World!'
# a2 = 'we are learning python'
# print(a1 + a2) # in the output we don't see any space between 2 string
# print(a1 + ' ' + a2) #in this output the space is created by using [' ']

                              ######End of Concatenation of strings###########
"""
Type conversion or type casting in python
Type casting means changing the types of one datatype into other datatype
exmaple: we can change integer into float and string
and we can also convert string or float into integers
Note: we can only convert the string into any integer or float when the string is having only numbers
without any other characters.
Note: if you are converting a float into integer then the value will be converted to the last rounding value.
below are the few example of those type casting.
"""

# a = 100
# print(a)
# print(type(a))
# #now the above variable is having int now we are changing into float by assigning 'a' to 'b' variables
# b = float(a)
# print(b)
# print(type(b))
# #now the int converted into float
# #converting float to integer
# c = 12.98
# print(c)
# print(type(c))
# #changing the float to integer
# d = int(c)
# print(d)
# print(type(d))
# #As you see it printed as 12 by rounding up not 13
# #now converting int into string and float into string
# e = 100
# print(e)
# print(type(e))
# f = 3.13
# print(f)
# print(type(f))
# g = str(e)
# print(g)
# print(type(g))
# h = str(f)
# print(h)
# print(type(h))
# #now we will try to convert a string into float and integer
# ss = '100'
# print(ss)
# print(type(ss))
# hh = int(ss)
# print(hh)
# print(type(hh))
# #changed string into integer
# ii = '98.98'
# print(ii)
# print(type(ii))
# gh = float(ii)
# print(gh)
# print(type(gh))
# #changed into float from string
# if you want to convert the string which has alphabets you will get the error
# Name = 'hello'
# print(Name)
# print(type(Name))
# nn = int(Name) # you will get this error : {ValueError: invalid literal for int() with base 10: 'hello'}
# Name1 = 'Python3.13'
# nh = float(Name1) #you will get this error: {ValueError: could not convert string to float: 'Python3.13'}
"""
Now we need to join 2 variable which has one string and one float using type casting
Example: a = 'python' and b = 3.13 and we need the output of python3.13
"""
# a = 'python'
# print(a)
# print(type(a))
# b = 3.13
# print(b)
# print(type(b))
# c = str(print(a + str(b)))
# print(type(c))

"""
Now we will try to add 2 string number as it is a integers
example: val1 = '100' and val2 = '200' output before typecasting is '100200'
after typecasting is '300'
"""
# val1 = '100'
# print(val1)
# print(type(val1))
# val2 = '200'
# print(val2)
# print(type(val2))
# print("result of adding 2 variables before using typecasting:", val1 + val2)
# print(type(val1 + val2))
# print("result using typecasting on the 2 variables:", int(val1) + int(val2))
# print(type(int(val1) + int(val2)))

"""
Now we will try to type casting the boolean into other data type (int,float,str)
and other data type (int,str,float) into Boolean 
Note: From the other datatype if you want to convert into bool always print 'True'
only number 0 and float 0.0 will be print as False and in the string 'False' will be false.
"""
# print(bool(True)) # bool true
# print(bool(False)) #boolean false
# print(bool(0)) # integer 0 into bool
# print(bool(1)) #integer 1 into bool
# print(bool(1000)) #integer 1000 into bool
# print(bool(0.0)) #float 0.0 into bool
# print(bool(0.1)) #float 0.1 into bool
# print(bool(-100)) # negative integer into bool
# print(bool('hello')) #string into bool
# print(bool('False')) #string True into bool
# print(bool('True')) #string False into bool

"""
And now trying to convert boolean into float, integer, string.
in bool True will be True in String will be True
in bool False will be False in String will be False
"""

# print(int(True))
# print(int(False))
# print(float(True))
# print(float(False))
# print(str(True))
# print(str(False))

                            ########End of the Type Casting and Type Conversion######
"""
Python operations
operations are the operands uses operators is called operations
for example a = 10 and y = a + 20 here
a,y are variables
10, 20 are values
=, + are operators
and variables and values are called as operands
there are different types of operators
they are:
Arithmetic operator
"""

# #Arithmetic operator
# num1 = 10
# num2 = 3
# #addition operator '+'
# print(num1 + num2)
# #Subtraction operator '-'
# print(num1 - num2)
# #Multiplication operator '*'
# print(num1 * num2)
# #Division operator '/'
# print(num1 / num2) # Note: Division result will always be in float only.
# #floor division operator '//'
# print(num1 // num2) #Note: Floor division will be in integer because if the division is less than the remainder then the last quotient will be the answer
# #modulus operator '%'
# print(num1 % num2) #Note: Modulus operator gives you the remainder as the output
# print(10 % 5)
# #exponent operator '**'
# print(num1 ** num2) #Now in the operator 10*10*10 answer will be output
# print(5 ** 2) #5*5 is the answer
# print(3 ** 4) #3*3*3*3 is the answer
"""
Assignment operator '='
Assigning a value or a data to a variable using assign operator 
example: a = 10 and Name = Gopi
compound assigned operator { '+=', '-=', '*=', '/='}
using arithmetic operator with the assignment is called compound assign operator
example: if a = 10 and a += 10 then now a is 20.
if you got a doubt how a became 20 this 
compound assign works like this 
first we assign a value to a variable
and when we are using the compound assign operator
the variable is holding a value in it and that value will be done math according to the Arithmetic operator
and that result will re-assign to the same variable.
"""

# #Example of compound assign operators
# num3 = 10
# print(num3) # we assigned 10 to the num3
# num3 += 1
# print(num3) # here calculation will be num3 = num3 + 1. the result will update the num3 again
# num3 -= 6
# print(num3) # here calculation will be num3 = num3 - 6. the result will update the num3 again
# num3 *= 10
# print(num3) # here calculation will be num3 = num3 * 10. the result will update the num3 again
# num3 /= 20
# print(num3) # here calculation will be num3 = num3 / 20. the result will update the num3 again


######## End of Arithmetic operators and assignment along with compound assign operators######