''' Exercise #1 - solution. Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 220.0  # Replace ??? with a positive float of your choice.
AB = 20.0  # Replace ??? with a positive float of your choice.
BC = 10.0  # Replace ??? with a positive float of your choice.
AD = 15.0  # Replace ??? with a positive float of your choice.
DC = 35.0  # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
circumference = AB + BC + AD + DC
midsegment = (AB + DC) / 2
height = S / midsegment
print('Diameter is:', circumference)
print('Midsegment is:', midsegment)
print('Height is:', height)


#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'oxana'  # Replace ??? with a string of your choice.
# Write the rest of the code for question 2 below here.
formatted_name = my_name[0].upper() + my_name[1:].lower()
print('Hello', formatted_name + '!')


#########################################
# Question 3 - do not delete this comment
#########################################
number = '49'  # Replace ??? with a string of your choice.
# Write the rest of the code for question 3 below here.
if(int(number) % 7 == 0):
    print('I am', number, 'and I am divisible by 7')
else:
    print('I am', number, 'and I am not divisible by 7')


#########################################
# Question 4 - do not delete this comment
#########################################
text = 'tom'  # Replace ??? with a string of your choice.
copies = 3  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
str1 = text[1::2]
str2 = text[0::2]
new_str = str1 + str2
print(copies * new_str)


#########################################
# Question 5 - do not delete this comment
#########################################
name = 'droLtromedloV'  # Replace ??? with a string of your choice.
q = 4  # Replace ??? with a int of your choice.
# Write the rest of the code for question 5 below here.
if type(name) != str or type(q) != int or q < 0 or q >= len(name) or len(name) == 0:
    print('Error: illegal input!')
else:
    sub1 = name[:q]
    sub2 = name[q:]
    sub1 = sub1[::-1]
    sub2 = sub2[::-1]
    print(sub1, sub2)
