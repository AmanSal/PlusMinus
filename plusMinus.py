import math
import os
import random
import re
import sys


# Created the 'plusMinus' function below.

# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    pos_val, neg_val, zero_val = [], [], []
    for element in arr:
        if element < 0:
            neg_val.append(element)
        elif element > 0:
            pos_val.append(element)
        else:
            zero_val.append(element)
    print("{:.6f}".format(len(pos_val) / len(arr)))
    print("{:.6f}".format(len(neg_val) / len(arr), 6))
    print("{:.6f}".format(len(zero_val) / len(arr) , 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
