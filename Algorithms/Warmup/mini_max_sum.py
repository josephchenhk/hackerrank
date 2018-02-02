# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:29:39 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

def bubbleSort(arr):
    n = len(arr)
    while n>1:
        for m in range(n-1):
            if arr[m]>arr[m+1]:
                arr[m], arr[m+1] = arr[m+1], arr[m]
        n -= 1
    return arr

def miniMaxSum(arr):
    # Complete this function
    arr = bubbleSort(arr)
    return sum(arr[:-1]), sum(arr[1:])

if __name__ == "__main__":
    arr = [4, 5, 1, 2, 3]
    # print(bubbleSort(arr))
    miniMaxSum(arr) # expect: (10, 14)
    print("{} {}".format(*miniMaxSum(arr)))