# Written by Hannah Lormenyo
# This is a function that returns the sum of Triangular Numbers up-to-and-including the nth Triangular Number.


def triangular(n):
    if n < 0:
        acc_triangular = 0    # returns 0 for negative numbers
    else:
        acc_triangular = 0
        for i in range(1, n+1):
            tri_num = i*(i+1)/2      # relation to determine the ith triangular number
            acc_triangular = acc_triangular + tri_num      # accumulator for the sum of the ith triangular numbers

    return acc_triangular


print(triangular(4))
