# 24/11/2020 exercise 5

# string formatting
s = ' this is a string, yes it   is  '
s.split()  # split the string by spaces (consecutive spaces count as one)
s.split(',')  # split the string by ','
s.strip()  # removes all the spaces (including \n \r) from both end
s.rstrip()  # removes all the spaces (including \n \r) from the right
s.lstrip()  # removes all the spaces (including \n \r) from the left

# files
try:
    # can only read the file, raise an error if it doesn't exist
    with open('exercise-4.py', 'r') as f:
        all = f.read()  # read all file at once
        lines = f.readlines()  # get a list of all the lines
        for i in range(3):
            line = f.readline()  # line by line

    with open('exercise-4.py', 'a') as f:  # adds to the files if exist and creates it if it doesn't
        f.write('line1\n')  # adds a single line
        f.write('line2\n')

    with open('exercise-4.py', 'w') as f:  # replace the files if exist and creates it if it doesn't
        # adds all the lines in the array
        f.writelines(['line 1\n', 'line2\n'])
except:
    pass

# error handling
try:
    # raise an error of type ValueError with the message 'error'
    raise ValueError('error')
    print('will never print this')
except ValueError:  # will catch any ValueError
    print('value error handled')
except:  # will catch any error
    print('error handled')
finally:  # will happen no matter if there was an error or not
    print('this is the end')
