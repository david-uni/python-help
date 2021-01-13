''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################


def reverse_string(s):
    if not s:
        return s
    return reverse_string(s[1:]) + s[0]


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if not lst:
        return -1
    return lst[0] if find_maximum(lst[1:]) < lst[0] else find_maximum(lst[1:])


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n < 3:
        return n
    return climb_combinations(n - 2) + climb_combinations(n - 1)


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if cnt < 0 or (not s and cnt > 0):
        return False
    if len(s) + cnt == 0:
        return True
    diff = 1 if s[0] == '(' else -1 if s[0] == ')' else 0
    return is_valid_paren(s[1:], cnt + diff)


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    # you can add tests for your code here.

    assert(reverse_string("abc") == 'cba')
    assert(reverse_string("Hello!") == '!olleH')

    assert(find_maximum([9, 3, 0, 10]) == 10)
    assert(find_maximum([9, 3, 0]) == 9)
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
