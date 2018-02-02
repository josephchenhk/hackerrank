# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:12:42 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import random
import time

"""Recursion
"""
def simpleArraySum1(n, ar):
    # Complete this function
    if n==1:
        return ar[0]
    else:
        return ar[0] + simpleArraySum1(n-1, ar[1:])
    
"""Dynamic programming
"""
def simpleArraySum2(n, ar):
    memo = []
    memo.append(ar[0])
    # If we already have the result, just deliver it
    if n<=len(memo):
        return memo[n-1]
    # If we havn't calculated the result, we need to calculate it based on the
    # available results at hand.
    else:
        m = len(memo) # start from this
        while m<len(ar):
            memo.append(memo[-1]+ar[m])
            m += 1
        return memo[-1]

    

if __name__=="__main__":
    n = 971000
    ar = [random.random() for _ in range(n)]
    
    # Recursion can only calculated maximum n=971 (for n=972 will get maximum 
    # recursion depth exceeded error.)
#    tic = time.time()
#    result = simpleArraySum1(n, ar)
#    toc = time.time()
#    print("Elapsed time: {:.3f}".format(toc-tic))
#    print(result)
    
    # Dynamic programming is fine for n>971
    tic = time.time()
    result = simpleArraySum2(n, ar)
    toc = time.time()
    print("Elapsed time: {:.3f}".format(toc-tic))
    print(result)