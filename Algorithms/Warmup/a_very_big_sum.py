# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:43:34 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/a-very-big-sum/problem
"""

def aVeryBigSum(n, ar):
    # Complete this function
    # python doesn't handle very big number. So this challenge is useless.
    bigSum = 0
    for m in ar:
        bigSum += m
    return bigSum

if __name__=="__main__":
    n = 6
    ar = [5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    result = aVeryBigSum(n, ar)
    print(result)