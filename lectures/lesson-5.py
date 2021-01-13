# 22/11/2020 Lesson 5


# input from user in the shell
user_name = input('please enter your name: ')
user_number = int(input('please enter a number: '))
print(user_name, user_number)

# input from files
# 'r' stands for read, and there are more options (w - write, a - append)
f1 = open('./lectures/lesson-4.py', 'r')
s1 = f1.read()  # reads the entire file
print(s1)
f1.close()  # important to close to stop using the memory

with open('./lectures/lesson-4.py', 'r') as f2:
    for line in f2:
        print(line)  # will print the file line by line

with open('./lectures/lesson-4.py', 'r') as f3:
    for i in range(3):
        print(f3.readline())  # will print the first 3 line, one by one
with open('./lectures/lesson-4.py', 'r') as f4:
    lines = f4.readlines()
    print(lines)  # will print a list with all the files lines

# string formatting
s = '      test       '
s1 = s.strip()  # trim all whitespaces at the ends
s2 = s.rstrip()  # trim all whitespaces at the right end
s3 = s.lstrip()  # trim all whitespaces at the left end
s4 = 'test?'.strip('?')  # removes the received characters from the string
print(s1, s2, s3, s4, sep='\n')

# write to file
'''
with open('lesson-4.py', 'w') as f5:
    f5.write('this is a line from lesson 5')
    f5.write('\n')
    f5.write('another one' + '\n')
    f5.write('ant yet another\n')
'''

# exceptions
try:
    print('bla' + 4)
except TypeError:
    print('a TypeError has occurred')
except IndexError:
    print('an IndexError has occurred')
except:
    print('an error hes occurred')
finally:
    print('will always happen')

# raise Exceptions
'''
raise ValueError('error message')
raise Exception('new exception error message')
'''
