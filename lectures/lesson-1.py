# 25/10/2020 lesson 1

# as always we start a new programing language with printing 'Hello world!'
print('Hello World!')


# variables
x = 12  # setting the value 12 to a variable named x

# types: str (text), int(number), float(decimal number), bool (True / False);
# to get the variable type we use the following function
type(x)  # will return the type of the value stored in x
type(12)  # int
type(12.0)  # float
type('bla bla')  # str
type(True)  # bool

# operations
# we can do operations between different types , but NOT always
name = 'bob'
number = 3
result = name * number  # str * int = str
print(result)

# result = name + number # str + int = ERROR, to fix we convert the int to str as follow:
# str(number) will returns the text value of the number e.g 2.5 => '2.5'
result = name + str(number)
print(result)
# convert to int
textNumber = '3'
int(textNumber)  # convert to int


# the operations will accurse in the correct order, by the rules of math
result = number + number * number

# available operations
# + addition
2 + 3  # = 5
# - subtraction
2 - 3  # = -1
# * multiplication
2 * 3  # = 6
# ** power - we can use fractions for root moperations
2 ** 3  # = 8
# / division
2 / 3  # = 0.6666
# // integer division
2 // 3  # = 0
# % modulo - the reminder of a division
3 % 2  # = 1

# strings - an ordered sequence of characters
# you can get the character of a string by index (starts with 0), e.g:
text = 'Hello World!'
print(text[0])  # 'H'
# you can start from the end
print(text[-1])  # '!'

#  0   1   2   3   4
#  H   e   l   l   o
#  -5 -4  -3  -2  -1

# get the index of a specific character in a string (will return the first one found)
str.find(text, 'o')  # 4

# slice - get only a part of the string
s = text[1:5]  # from index 1 to index 5 NOT including 5
print(s)  # 'ello'
# up to index
s = text[:5]  # up to index 5 Not including
print(s)  # 'Hello'
# from index to end
s = text[6:]  # from index 6 to the end
print(s)  # 'World!'

#slicing and jumping
# slice from index 2 to index 8, and the returning every 2nd character
s = text[2:8:2]
print(text[2:8])
print(s)  # 'loW'

# get the len of a string
len(text)
# transform string to lower case
str.lower(text)  # 'HELLO WORLD!'
# transform string to upper case
str.upper(text)  # 'hello world!'
str.replace(text, '!', '?')  # replace all the '!' with '?'
str.title(text)  # capitalize the first letter

# comparison operators
1 < 2  # 1 less than 2 => True
1 > 2  # 1 greater than 2 => False
1 <= 2  # 1 less or equals to 2 => True
1 >= 2  # 1 greater or equal to 2 => False
1 == 2  # 1 equals to 2 => False
1 != 2  # 1 not equal to 2 => True

# logical operators (and, or, not)
# and
True and True  # True
True and False  # False
False and False  # False
# or
True or True  # True
True or False  # True
False or False  # False
# not
not True  # False
not False  # True

# flow control (if-else, for, while)
# if-else
condition1 = True
condition2 = True
if condition1:
    test = 0
    #
    # will do if condition resolve to True
    #
elif condition2:
    test = 1
    #
    # will do if the new condition resolve to true
    #
else:
    test = 2
    #
    # will do if all the conditions up to now resolved to False
    #

# for
for i in range(10):
    test = i
    #
    # will happen 10 times
    #
