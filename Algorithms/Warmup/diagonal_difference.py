# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:53:39 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

def diagonalDifference(a):
    # Complete this function
    diag = 0
    r_diag = 0 # reverse diagonal
    for n in range(len(a)):
        diag += a[n][n]
        r_diag += a[n][-1-n]
    return abs(diag - r_diag)

if __name__ == "__main__":
    n = 3
    a = [[11, 2, 4],
         [4, 5, 6],
         [10, 8, -12]
        ]
    result = diagonalDifference(a)
    print(result)