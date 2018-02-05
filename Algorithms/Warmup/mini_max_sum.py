# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:29:39 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

def bubbleSort(arr):
    # each time move the largest number to the end (bubble up)
    n = len(arr)
    while n>1:
        for m in range(n-1):
            if arr[m]>arr[m+1]:
                arr[m], arr[m+1] = arr[m+1], arr[m]
        n -= 1
    return arr

def insertionSort(arr):
    # each time insert an element to a sorted list, until the length of sorted 
    # list equals to the original list
    if len(arr)==1:
        return arr
    else:
        for i in range(1,len(arr)):
            elem = arr[i]
            for j in range(i-1,-1,-1): # from (i-1) to 0
                if arr[j]>elem:
                    arr[j+1] = arr[j]
                    arr[j] = elem
                else:
                    break
        return arr

def miniMaxSum(arr):
    # Complete this function
    # arr = bubbleSort(arr)
    arr = insertionSort(arr)
    return sum(arr[:-1]), sum(arr[1:])

if __name__ == "__main__":
    arr = [4, 5, 1, 2, 3]
    # print(bubbleSort(arr))
    # print(insertionSort(arr))
    miniMaxSum(arr) # expect: (10, 14)
    print("{} {}".format(*miniMaxSum(arr)))