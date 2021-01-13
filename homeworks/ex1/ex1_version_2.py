''' Exercise #1 - solution. Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 12.0  # Replace ??? with a positive float of your choice.
AB = 2.0  # Replace ??? with a positive float of your choice.
BC = 5.0  # Replace ??? with a positive float of your choice.
AD = 5.0  # Replace ??? with a positive float of your choice.
DC = 10.0  # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.


def calc_trapezoid_circumference(a, b, c, d):
    return a + b + c + d


def calc_trapezoid_midsegment(a, c):
    return (a + c) / 2


def calc_trapezoid_height(area, a, c):
    return area / calc_trapezoid_midsegment(a, c)


print('Diameter is:', calc_trapezoid_circumference(AB, BC, AD, DC))
print('Midsegment is:', calc_trapezoid_midsegment(AB, DC))
print('Height is:', calc_trapezoid_height(S, AB, DC))


#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'David'  # Replace ??? with a string of your choice.
# Write the rest of the code for question 2 below here.


def greetings(name):
    print('Hello', name[0].upper() + name[1:].lower() + '!')


greetings(my_name)


#########################################
# Question 3 - do not delete this comment
#########################################
number = '-14'  # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.


def is_divisible_by(number, division):
    if(int(number) % division == 0):
        print('I am', number, 'and I am divisible by', division)
    else:
        print('I am', number, 'and I am not divisible by', division)


is_divisible_by(number, 7)


#########################################
# Question 4 - do not delete this comment
#########################################
text = '01234'  # Replace ??? with a string of your choice.
copies = 2  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.


def separate_and_recombine_odd_even(string, num_copies):
    odd = string[1::2]
    even = string[::2]
    return (odd + even) * num_copies


print(separate_and_recombine_odd_even(text, copies))


#########################################
# Question 5 - do not delete this comment
#########################################
name = 'etaergsseccus'  # Replace ??? with a string of your choice.
q = 6  # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.


def is_input_valid(name, q):
    if type(name) != str or type(q) != int or q < 0 or q >= len(name) or len(name) == 0:
        return False
    return True


def exercise_5(name, q):
    if(not is_input_valid(name, q)):
        print('Error: illegal input!')
    else:
        sub1 = name[:q][::-1]
        sub2 = name[q:][::-1]
        print(sub1, sub2)


exercise_5(name, q)
