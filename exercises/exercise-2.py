# 3/11/2020 exercise 2


# strings - useful functions
s = 'While my guitar gently weeps'
s.lower()
# returns the index of the first time 'e' exist in the string, -1 if it doesn't
s.find('e')
s.count('e')  # returns the number of time 'e' exist in the string

# lists -  a collection of elements in a specific order
empty_list = []
# creates a list with the length of 100 and all the elements set to 0
initialize_list = [0] * 100

my_list = [2, 3, 4]
my_list.insert(0, 1)  # inserts at index 0 the value 1
my_list.append(5)  # adds the value 5 to the end of the list
# appends the new every element in the list [6, 7, 8] to the end of my_list
my_list.extend([6, 7, 8])
my_list[len(my_list) - 1] = 8.0  # replace the value at the last index
my_list[0:3] = [0, 1, 2]  # replace the entire slice with the new elements
# can be used to remove elements - replace the entire slice with nothing
my_list[0:3] = []
# removes the value 8.0 the first time it appears, throw an error if it doesn't exist
my_list.remove(8.0)

4 in my_list  # return if the value 4 exist in my_list
my_list.reverse()  # reverse the order of the element in the list
my_list.sort()  # sort the element in the list (default by ascii)


# for loops
my_list = [1, 2, 3, 4, 5]
my_sum = 0
for element in my_list:
    my_sum += element

print('first', end=' ')  # instead of \r at the end, print will add ' '
print('second', '!', sep='')  # replace the default seperator (' ') with ''

# to get both index and element we can use enumerate
for i, elem in enumerate(my_list):
    print(i, ':', elem, ', ', sep='', end='')

print(list(enumerate(my_list)))

my_input = int(input('please enter a number:'))
print('your number is:', my_input)


print('------------------------------------------------------------------------------------')

# exercise 1
print("--------------- find a contact ------------------")


phone_book = [['nir', '7886'],
              ['moshe', '123321'],
              ['cohen', '0123456758'],
              ['niv', '343345'],
              ['niel', '545'],
              ['neigel', '78654686']]

# Retrieve the number for a given person
name = "moshe"
found = False
phone = ''
for contact in phone_book:
    if contact[0] == name:
        found = True
        phone = contact[1]
        break
if found:
    print("Name:", name, "Phone:", phone)
else:
    print("Cannot find", name, "in contact list.")

print("--------------- append contact -------------------------")

# Add a contact
name = "dan"
num = 1454
phone_book.append([name, num])

# copy the first part and search for new contact "dan"

print("------------------ remove a contact ----------------------")


# Remove a contact
name = "moshe"
found = False
for contact in phone_book:
    if contact[0] == name:
        phone_book.remove(contact)
        found = True
        break
if not found:
    print("Cannot find contact")

# copy the first part and search for deleted contact "moshe"

print("----------------------------------------")

##################
# for-else: if loop ended because of break go to else
##################
# Remove a contact using a for-else construct
name = "nir"
for contact in phone_book:
    if contact[0] == name:  # Found it!
        phone_book.remove(contact)
        break
else:  # Didn't find anything..
    print("Cannot find contact")

# copy the first part and search for deleted contact "nir"


print("----------------------------------------")

# Search for all contacts with given prefix.
# Ignore character case (aka, case insensitive).
prefix = "Ni"
prefix = prefix.lower()  # Ignore character case
for contact in phone_book:
    if contact[0].lower().startswith(prefix):  # use .startswith(prefix)
        print("Name:", contact[0], "Phone:", contact[1])

print("----------------------------------------")
