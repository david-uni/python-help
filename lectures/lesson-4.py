# 15/11/2020 Lesson 4

# tuples
def example():
    return 1, 2, 3  # will return a tuple - e.g. (1, 2, 3)


my_tuple = (1, 2)  # immutable


# dictionaries
my_dict = {'key': 'val'}
my_dict['key']
# default in case none existing - None
my_dict.get('key', 'value in case key doesn\'t exist')
my_dict.keys()  # returns a dynamic list of all the key
my_dict.values()  # returns a dynamic list of all the value
my_dict.items()  # returns a dynamic list of all the key, value pair as tuples
my_dict_keys = my_dict.keys()

print(my_dict_keys)
my_dict['new_key'] = 'new val'
# you can see that the keys are dynamic and now contains the new_key
print(my_dict_keys)

# returns a boolean (True - if it is, False - if it isn't)
'new_key' in my_dict

my_dict.pop('new_key', 'return value if the key doesn\'t exist')
copy_dict = my_dict.copy()
{}.update(my_dict)  # add all the keys and values of my_dict to {}
