# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:08:34 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/plus-minus/problem
"""

def plusMinus(arr):
    # Complete this function
    pos = 0
    neg = 0
    zero = 0
    for a in arr:
        if a>0:
            pos += 1
        elif a<0:
            neg += 1
        else:
            zero += 1
    N = len(arr)*1.0
    return pos/N, neg/N, zero/N

if __name__ == "__main__":
    n = 6
    arr = [-4, 3, -9, 0, 4, 1]
    # plusMinus(arr) # expect [0.5000, 0.3333, 0.1667]
    results = plusMinus(arr)
    for res in results:
        print(res)