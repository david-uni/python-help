''' Exercise #6. Python for Engineers.'''


#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n < 4:
        return n
    return sum(four_bonacci_rec(n - i) for i in range(1, 5))


#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if memo == None:
        memo = {0: 0, 1: 1, 2: 2, 3: 3}
    if n not in memo:
        memo[n] = sum(four_bonacci_mem(n - i, memo) for i in range(1, 5))
    return memo[n]


#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if memo == None:
        memo = {0: 1, 1: 1}
    if n not in memo:
        memo[n] = sum(climb_combinations_memo(n-i, memo) for i in range(1, 3))
    return memo[n]


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n, memo=None):
    if memo == None:
        memo = {0: 1}
    if n not in memo:
        memo[n] = sum([catalan_rec(i, memo) * catalan_rec(n - 1 - i, memo)
                       for i in range(n)])
    return memo[n]


#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n == 0:
        return 1
    if n < 0 or len(lst) == 0:
        return 0
    return find_num_changes_rec(n-lst[0], lst) + find_num_changes_rec(n, lst[1:])


#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n == 0:
        return 1
    if n < 0 or len(lst) == 0:
        return 0
    if memo == None:
        memo = {}
    key = (n, len(lst))
    if key not in memo:
        memo[key] = find_num_changes_mem(
            n-lst[0], lst, memo) + find_num_changes_mem(n, lst[1:], memo)
    return memo[key]


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Question 1.a tests - you can and should add more
    """
    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)
    """
    # Question 1.b tests - you can and should add more
    """
    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)
    """
    # Question 2 tests - you can and should add more
    """
    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    """
    # Question 3 tests - you can and should add more
    """
    cat_list = [1, 1, 2, 5, 14, 42, 132, 429]
    for n, res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    """
    # Question 4.a tests - you can and should add more
    """
    print(find_num_changes_rec(5, [1, 2, 5, 6]) == 4)
    print(find_num_changes_rec(4, [1, 2, 5, 6]) == 3)
    print(find_num_changes_rec(0.9, [1, 2, 5, 6]) == 0)
    print(find_num_changes_rec(105, [1, 105, 999, 100]) == 3)
    """
    # Question 4.b tests - you can and should add more
    """
    print(find_num_changes_mem(5, [1, 2, 5, 6]) == 4)
    print(find_num_changes_mem(4, [1, 2, 5, 6]) == 3)
    print(find_num_changes_mem(105, [1, 105, 999, 100]) == 3)
    """
    pass
# ============================== END OF FILE =================================
