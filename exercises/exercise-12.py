# 012/01/2021 exercise 12
import pandas as pd  # importing the pandas library with the alias 'pd'
import numpy as np


# Question 1 - Asset Partition
def assets_partition(assets, s1=0, s2=0):
    if not assets:
        return s1 == s2
    return assets_partition(assets[1:], s1 + assets[0], s2) or \
        assets_partition(assets[1:], s1, s2 + assets[0])


# Question 1 - Asset Partition with Memo
def assets_partition_memo(assets, s1=0, s2=0, memo=None):
    if not assets:
        return s1 == s2
    if memo == None:
        memo = {}
    key = (len(assets), s1)
    if key not in memo:
        memo[key] = assets_partition_memo(assets[1:], s1 + assets[0], s2, memo) or \
            assets_partition_memo(assets[1:], s1, s2 + assets[0], memo)
    return memo[key]


# Question 2 - Cafe Orders
def load_orders(orders_csv, prices_csv):
    orders = pd.read_csv(orders_csv)
    prices = pd.read_csv(prices_csv)
    return orders, prices


def print_orders():
    orders, prices = load_orders('orders.csv', 'prices.csv')
    print(f'number of ...: {orders.sum().sum()}')


def print_more_than_2_orders():
    orders, prices = load_orders('orders.csv', 'prices.csv')
    orders_per_custoemer = (orders > 0).sum(axis=1)
    print(
        f'number of customers that ordered more than 2 different products: {(orders_per_custoemer > 2).sum()}')


def to_do():
    pass


def print_total_revenue():
    orders, prices = load_orders('orders.csv', 'prices.csv')
    # ndarray.dot(ndarray) returns the mathematic solution to matrix multiplication
    print(f'total revenue: {orders.dot(prices.T).sum().sum()}')


def to_do_more():
    pass


# Question 3 - Pixelize Image
def pixelize_image(im, k):
    new_im = np.zeros(im.shape)
    for i in range(0, im.shape[0], k):
        for j in range(0, im.shape[1], k):
            new_im[i:i + k, j:j + k] = im[i:i + k, j:j + k].mean()
    return new_im


# Question 4 - Submarines
class Subs(object):
    def __init__(self, table, ships):
        self.table = table
        self.ships = ships

    def __repr__(self):
        return ''.join([f'TODO{i+j}\n' for j in self, tables for i in tables])

    def is_alive_in_dir(self, x, y, dx, dy):
        pass

    def hit(self, x, y):
        pass
