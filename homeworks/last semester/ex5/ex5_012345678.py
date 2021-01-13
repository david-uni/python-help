''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    pass  # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    pass  # replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    pass  # replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    pass  # replace this with your implementation


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    pass  # replace this with your implementation


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9,3,0,10]) == 10)
print(find_maximum([9,3,0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") == True)
print(is_palindrome("aa ") == False)
print(is_palindrome("caca") == False)
print(is_palindrome("abcbbcba") == True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)

print(is_valid_paren("(.(a)") == False)
print(is_valid_paren("p(()r((0)))") == True)

# ============================== END OF FILE =================================
