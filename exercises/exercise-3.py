# 10/11/2020 exercise 3

lst = [1, 2, [3, 4]]
for elem in lst:
    if type(elem) == list and len(elem) > 0:
        elem[0] = None
print(lst)
for elem in lst:
    elem = 0
print(lst)


def test(val):
    '''this is the documentation of the function'''
    return val


help(test)  # returns the documentation of the function
