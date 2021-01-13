''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    pass




#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    pass




#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    pass




#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    pass




#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    pass



#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    #you can add tests for your code here.
    
    assert(reverse_string("abc") == 'cba')
    assert(reverse_string("Hello!") == '!olleH')

    assert(find_maximum([9,3,0,10]) == 10)
    assert(find_maximum([9,3,0]) == 9)
    assert(find_maximum([]) == -1)

    assert(is_palindrome("aa") == True)
    assert(is_palindrome("aa ") == False)
    assert(is_palindrome("caca") == False)
    assert(is_palindrome("abcbbcba") == True)

    assert(climb_combinations(3) == 3)
    assert(climb_combinations(10) == 89)

    assert(is_valid_paren("(.(a)") == False)
    assert(is_valid_paren("p(()r((0)))") == True)
    assert(is_valid_paren("") == True)

# ============================== END OF FILE =================================
