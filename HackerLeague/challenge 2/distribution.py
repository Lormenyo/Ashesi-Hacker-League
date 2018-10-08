# By Hannah Boadiwaa Lormenyo
# 1st October 2018

import numpy as np


def distribute(m, n):
    share = []
    if n <= 0:
        return share
    elif m <= 0:
        share = np.zeros(n, dtype='int')
    elif m < n and n >= 0:
        share = np.ones(n, dtype='int')
        share[m:n] = np.zeros(m, dtype='int')
    elif m == n:
        share = np.ones(n, dtype='int')
    else:
        share = np.ones(n, dtype='int') * (int(m/n))
        for i in range(m % n):
            share[i] = share[i] + 1
    return list(share)


print(distribute(-5, 0))
print(distribute(0, 0))
print(distribute(5, 0))
print(distribute(10, 0))
print(distribute(15, 0))
print(distribute(-5, -5))
print(distribute(0, -5))
print(distribute(5, -5))
print(distribute(10, -5))
print(distribute(15, -5))
print(distribute(-5, 10))
print(distribute(0, 10))
print(distribute(5, 10))
print(distribute(10, 10))
print(distribute(15, 10))
print(distribute(100000, 1000))
print(distribute(19, 10))