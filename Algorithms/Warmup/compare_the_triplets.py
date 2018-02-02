# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:25:14 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = 0
    B = 0
    
    if a0>b0:
        A += 1
    elif a0<b0:
        B += 1
        
    if a1>b1:
        A += 1
    elif a1<b1:
        B += 1 
        
    if a2>b2:
        A += 1
    elif a2<b2:
        B += 1
        
    return A,B

if __name__=="__main__":
    a0, a1, a2 = [5,6,7]
    b0, b1, b2 = [3,6,10]
    result = solve(a0, a1, a2, b0, b1, b2)
    print (" ".join(map(str, result)))