""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 7  # Replace the assignment with a positive integer to test your code.
# Replace the assignment with other lists to test your code.
lst = [10, 20, 5, 7]

# Write the rest of the code for question 1 below here.


def first_divisible_by(lst, num):
    for i, val in enumerate(lst):
        if val % num == 0:
            return i
    return -1


print(first_divisible_by(lst, a))


# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['55555', '55555', '666666', '666666', '333']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.

def get_average_length_for(lst):
    return len(''.join(lst)) / len(lst)


def above_average_using_for(lst):
    average = get_average_length_for(lst)
    counter = 0
    for val in lst:
        if len(val) > average:
            counter += 1
    return counter


print('The number of stringslonger than the average is:',
      above_average_using_for(lst2))

# Write the code for question 2 using a while loop below here.


def get_average_length_while(lst):
    return len(''.join(lst)) / len(lst)


def above_average_using_while(lst):
    average = get_average_length_while(lst)
    counter = 0
    i = 0
    while i < len(lst):
        if len(lst[i]) > average:
            counter += 1
        i += 1
    return counter


print('The number of stringslonger than the average is:',
      above_average_using_while(lst2))

# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

# Replace the assignment with other lists to test your code.
lst3 = [1, -2, 3, -4, 5]


# Write the rest of the code for question 3 below here.
def list_multiplication(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    my_sum = 0
    for i in range(len(lst) - 1):
        my_sum += lst[i] * lst[i + 1]
    return my_sum


print(list_multiplication(lst3))

# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

# Replace the assignment with other lists to test your code.
lst4 = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5, 6, 7, 8, 9, 10, 15]

# Write the rest of the code for question 4 below here.


def max_diff(lst):
    new_list = lst[:2]
    for i in range(2, len(lst)):
        if abs(lst[i] - new_list[-1]) > abs(new_list[-1] - new_list[-2]):
            new_list.append(lst[i])
    return new_list


print(max_diff(lst4))

# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

# Replace the assignment with other strings to test your code.
my_string = 'abbcccddddeeeeeffffggghhi'
k = 4  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.


def match_str_to_length(string, length):
    accumulator = ''
    for char in list(string):
        if len(accumulator) == 0 or accumulator[-1] == char:
            accumulator += char
        else:
            accumulator = char
        if len(accumulator) == length:
            return f'For length {length}, found the substring {accumulator}!'
    return f'Didn\'t find a substring of length {length}'


print(match_str_to_length(my_string, k))
# End of code for question 5
