# 17/11/2020 exercise 4

# dictionaries
my_dict = {}  # creating and initializing it
# convert a list with tuples of (key, value) into a dictionary
new_dict = dict([('a', 1), (2, 'b'), (True, 0)])
# add all the key-value pairs from new_dict into my_dict
my_dict.update(new_dict)

for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

my_dict['a']
my_dict.get('test')
my_dict.pop('test', 'Not found')
