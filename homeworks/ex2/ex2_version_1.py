""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 3  # Replace the assignment with a positive integer to test your code.
# Replace the assignment with other lists to test your code.
A = [1, 2, 3, 4, 5]

# Write the rest of the code for question 1 below here.
found = False
for i in range(len(A)):
    if A[i] % a == 0:
        found = True
        break
if found:
    print(i)
else:
    print(-1)

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
B = ['hello', 'world', 'course', 'python', 'day']
# Replace the assignment with other lists of strings (str) to test your code.
combined_words = ''
for i in B:
    combined_words += i
average_word_length = len(combined_words) / len(B)

# Write the code for question 2 using a for loop below here.
count = 0
for i in B:
    if len(i) > average_word_length:
        count += 1
print('The number of strings longer than the average is:', count)

# Write the code for question 2 using a while loop below here.
count = 0
i = 0
while i < len(B):
    if len(B[i]) > average_word_length:
        count += 1
    i += 1
print('The number of strings longer than the average is:', count)


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

# Replace the assignment with other lists to test your code.
C = [0, 1, 2, 3, 4]

# Write the rest of the code for question 3 below here.
if (len(C) == 0):
    print(0)
elif len(C) == 1:
    print(C[0])
else:
    result = 0
    for i in range(len(C) - 1):
        result += C[i] * C[i + 1]
    print(result)

# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

# Replace the assignment with other lists to test your code.
D = [1, 2, 0, -3, 1, -4, 2, -5, 3, -6, 4, 5]

# Write the rest of the code for question 4 below here.
new_list = [D[0]]
max_diff = 0
for i in range(1, len(D)):
    current_diff = abs(new_list[-1] - D[i])
    if current_diff > max_diff:
        new_list.append(D[i])
        max_diff = current_diff
print(new_list)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

# Replace the assignment with other strings to test your code.
my_string = 'abaadddefggg'
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
did_found = False
current_length = 1
current_substring = my_string[0]
if k == 1:
    print('For length', k, 'found the substring', current_substring + '!')
    did_found = True
else:
    for i in range(1, len(my_string)):
        if my_string[i - 1] == my_string[i]:
            current_substring += my_string[i]
            current_length += 1
            if k == current_length:
                print('For length', k, 'found the substring',
                      current_substring + '!')
                did_found = True
                break
        else:
            current_length = 1
            current_substring = my_string[i]
if not did_found:
    print('Didn\'t find a substring of length', k)

# End of code for question 5
