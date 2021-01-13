# 01/12/2020 exercise 6

# recursion
def sum_of_digits(num):
    if num < 10:
        return num
    return num % 10 + sum_of_digits(num // 10)


print(sum_of_digits(1204))


def fast_power(base, power):
    if not power:
        return 1
    return base * fast_power(base, power - 1) if power % 2 != 0 else fast_power(base, power / 2) ** 2


print(fast_power(2, 5))


def choose(n, k):
    if k == 0 or n == k:
        return 1
    if n < k:
        return 0
    if k == 1:
        return n
    return choose(n - 1, k) + choose(n - 1, k - 1)


print(choose(4, 2))


def sub_list_sum(lst, sm):
    if sm == 0:
        return True
    if len(lst) == 0:
        return sm == 0
    return sub_list_sum(lst[1:], sm-lst[0]) or sub_list_sum(lst[1:], sm)


print(sub_list_sum([1, 3, 2, 4], 9))


def reverse_num(num, res=0):
    if num == 0:
        return res
    return reverse_num(num // 10, res * 10 + num % 10)


print(reverse_num(1234))
