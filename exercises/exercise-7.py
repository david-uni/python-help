# 08/12/2020 exercise 6

import random


def get_random_price(start=0, limit=200):
    return random.randint(start, limit)


def generate_prices(start, end):
    return {(i, j): get_random_price()
            for i in range(start, end) for j in range(i + 1, end + 1)}


def best(start, end):
    prices = generate_prices(start, end)

    def best_rec(start, end, prices, memo=None):
        if start == end:
            return 0
        if memo == None:
            memo = {}
        if start in memo:
            return memo[start]
        memo[start] = min(prices[(start, i)] + best_rec(i,
                                                        end, prices, memo) for i in range(start + 1, end + 1))
        return memo[start]

    return best_rec(start, end, prices), 'vs', prices[(start, end)]


print(best(1, 50))


prices = {(1, 2): 5, (1, 3): 5, (1, 4): 10, (1, 5): 9,
          (2, 3): 1, (2, 4): 7, (2, 5): 12, (3, 4): 4, (3, 5): 2, (4, 5): 6}


def best_rout(start, end, prices, memo=None):
    if start == end:
        return 0, []
    if memo == None:
        memo = {}
    options = []
    for i in range(start + 1, end + 1):
        price, trail = best_rout(i, end, prices, memo)
        acc_price = prices[(start, i)] + price
        acc_trail = [[start, i], *trail]
        options.append((acc_price, acc_trail))
    help_dict = {i: option[0] for i, option in enumerate(options)}
    memo[start] = options[min(help_dict, key=help_dict.get)]
    return memo[start]


for i in range(1, 5):
    print(best_rout(i, 5, prices))


def is_merge(combined, str1, str2, memo=None):
    if not str1:
        return combined == str2
    if not str2:
        return combined == str1
    if not combined:
        return False
    if memo == None:
        memo = {}
    key = (len(str1), len(str2))
    if key not in memo:
        memo[key] = (str1[0] == combined[0] and is_merge(combined[1:], str1[1:], str2, memo)) or (
            str2[0] == combined[0] and is_merge(combined[1:], str1, str2[1:], memo))
    return memo[key]


cases = [('good luck', 'go uk', 'odlc'), ('aabaaaaad', 'aaaaaa', 'bad'),
         ('not merge', 'not ', 'not merge'), ('not merge either', 'a', 'b')]
for case in cases:
    print(case[0], '-', is_merge(*case))


def merge_sort(lst, order='ascending'):
    if len(lst) < 2:
        return lst
    return merge(merge_sort(lst[:len(lst) // 2], order), merge_sort(lst[len(lst) // 2:], order), order)


def merge(lst1, lst2, order):
    order_options = ['ascending', 'descending']
    if order not in order_options:
        raise ValueError(f'unsupported order: {order}')
    sorted_list = []
    i1 = 0
    i2 = 0
    while i1 < len(lst1) and i2 < len(lst2):
        if (order == 'ascending' and lst1[i1] <= lst2[i2]) or (order == 'descending' and lst1[i1] >= lst2[i2]):
            sorted_list.append(lst1[i1])
            i1 += 1
        else:
            sorted_list.append(lst2[i2])
            i2 += 1
    sorted_list += lst1[i1:] + lst2[i2:]
    return sorted_list


lists = [[1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1], [1, 7, 3, 5, 3, 2, 8]]
for lst in lists:
    print(merge_sort(lst), '- ascending')
    print(merge_sort(lst, 'descending'), '- descending')
