''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    pass #replace this with your implementation


#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    pass #replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    pass #replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    pass #replace this with your implementation
    

#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    pass #replace this with your implementation
    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    pass #replace this with your implementation


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

#Question 1.a tests - you can and should add more    
print(four_bonacci_rec(0) == 0)
print(four_bonacci_rec(5) == 12)
print(four_bonacci_rec(8) == 85)

#Question 1.b tests - you can and should add more    
print(four_bonacci_mem(0) == 0)
print(four_bonacci_mem(5) == 12)
print(four_bonacci_mem(8) == 85)

#Question 2 tests - you can and should add more    
print(climb_combinations_memo(4) == 5)
print(climb_combinations_memo(42) == 433494437)

#Question 3 tests - you can and should add more    
cat_list = [1,1,2,5,14,42,132,429]
for n,res in enumerate(cat_list):
    print(catalan_rec(n) == res)

#Question 4.a tests - you can and should add more        
print(find_num_changes_rec(5,[1,2,5,6]) == 4)
print(find_num_changes_rec(4,[1,2,5,6]) == 3)
print(find_num_changes_rec(0.9,[1,2,5,6]) == 0)

#Question 4.b tests - you can and should add more        
print(find_num_changes_mem(5,[1,2,5,6]) == 4)
print(find_num_changes_mem(4,[1,2,5,6]) == 3)
print(find_num_changes_mem(0.9,[1,2,5,6]) == 0)

# ============================== END OF FILE =================================