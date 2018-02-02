# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:19:45 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/staircase/problem
"""

def staircase(n):
    # Complete this function
    for k in range(n):
        print(" "*(n-k-1) + "#"*(k+1))

if __name__ == "__main__":
    n = 4
    staircase(n)