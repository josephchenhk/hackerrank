# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:19:35 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/marcs-cakewalk/problem
"""

def marcsCakewalk(calorie):
    # Complete this function
    calorie.sort(reverse=True)
    walk = 0
    for n,c in enumerate(calorie):
        walk += c*2**n
    return walk
    

if __name__ == "__main__":
    n = 3
    calorie = [1, 3, 2]
    result = marcsCakewalk(calorie)
    print(result)