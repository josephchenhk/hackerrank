# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:26:53 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
"""


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

def mergeSort(arr):
    """
    https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
    """
    # Each time merge two sorted list to a new combined sorted list
    if len(arr)==1:
        return arr
    else:
        midpoint = len(arr)//2
        left = mergeSort(arr[:midpoint])  # left sorted list
        right = mergeSort(arr[midpoint:])  # right sorted list 
        print(left, "|" , right)
        return merge(left, right)
        
def merge(left, right):
    combine = []
    while len(left)>0 and len(right)>0:
        if left[0]>right[0]:
            combine.append(right[0])
            right = right[1:]
        else:
            combine.append(left[0])
            left = left[1:]
    
    while len(left)>0:
        combine.append(left[0])
        left = left[1:]
        
    while len(right)>0:
        combine.append(right[0])
        right = right[1:]
        
    return combine
                      
                      
def minimumAbsoluteDifference(n, arr):
    # Insertion sorting fails here
    # arr = insertionSort(arr)
    
    # Merge sort also fails
    # arr = mergeSort(arr)
    
    # Python built-in sort() works (Timsort)
    arr.sort()
    
    diff = [b-a for (a,b) in zip(arr[0:-1],arr[1:])]
    return min(diff)


if __name__ == "__main__":
    n = 3
    arr = [3, -7, 0]
    #print(mergeSort(arr))
    result = minimumAbsoluteDifference(n, arr)
    print(result)