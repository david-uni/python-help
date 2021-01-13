# 01/11/2020 Lesson 2
import math

# string formating
name = 'David'
pi = math.pi
formated_str = 'My name is {0} and I like {1}'.format(name, pi)
print(formated_str)
formated_str = 'My name is {0} and I like {1:.2f}'.format(
    name, pi)  # convert to float with 2 decimals values
print(formated_str)
# a shorter way to use string formatting
formated_str = f'My name is {name} and I like {pi:.2f}'
print(formated_str)


# lists
my_list = [0, '1', 2.0]  # saves the order
my_list[0]
my_list[:]  # the entire list from the beginning till the end
my_list[::2]  # only odd indexes
# when using negative 'jumps' the indexes can be omitted, or reversed
my_list[len(my_list):0:-1]
my_list.append(3)  # adds the value 3 to the end of the list
my_list.remove(2.0)  # removes the first time the value 2.0 exist in the list
my_list.pop()  # removes the the value at the end of the list (last index)
my_list.pop(1)  # removes the the value at index=1 from the list

# 2 dimensions list
my_list = [[1, 2, 3],
           [4, 5, 6]]
my_list[0][0]  # the value at row 0 and column 0

# sorting
first_list = [5, 2, 3, 1, 0]
second_list = ['5', '2', '3', '1', '10']
first_list.sort()  # sorts the list itself, from now on first_list is sorted
# returns a copy of the sorted list, second_list is still with the same order it was
sorted(second_list)
sorted(second_list, key=len)  # sort the list by the given function

# split string
s = 'I am David'
s_list = s.split()  # splits the string into a list by spaces
s_list = s.split(' ')  # splits the string into a list by the given value


# loops
# for
my_sum = 0
for i in [3, 5, 7, 9, 10]:
    my_sum += i  # i is equals to the value at the current index

# range
list(range(10))  # creates a list of numbers from 0 up to 9
list(range(1, 11))  # creates a list of numbers from 1 up to 10

my_sum = 0
for i in range(10):
    my_sum += i

# while - beware that if the expression never returns False the loop will never end
n = 7
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print(str(n) + '! =', fact)

print(sum(range(1, 101)))  # the function sum() is built into python


def fibonacci(n):
    my_fibonacci = [1, 1]
    for i in range(n-2):
        my_fibonacci.append(my_fibonacci[i] + my_fibonacci[i+1])
    return my_fibonacci


# continue & break
def even_numbers(my_list):
    evens = []
    for i in my_list:
        if i % 2 != 0:
            continue
        evens.append(i)
    print(evens)


even_numbers([1, 2, 3, 4, 5, 6, 2, 4, 5])


def prime_number(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            break
    if number % i == 0:
        print(number, 'is not prime')
    else:
        print(number, 'is prime')


prime_number(121)
