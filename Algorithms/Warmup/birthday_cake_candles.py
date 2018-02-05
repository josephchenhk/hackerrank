# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:31:09 2018

@author: joseph.chen
"""

def birthdayCakeCandles(n, ar):
    # This method uses the built-in functions
    return ar.count(max(ar))

def birthdayCakeCandles(n, ar):
    # Let's just build it from scratch
    max_count = [ar[0], 1]  # [max, count]
    if len(ar)==1:
        return 1
    else:
        for i in range(1,len(ar)):
            if ar[i]>max_count[0]:
                max_count = [ar[i], 1]
            elif ar[i]==max_count[0]:
                max_count = [max_count[0], max_count[1]+1]
    return max_count[1]

if __name__=="__main__":
    n = 4
    ar = [3, 2, 1, 3]
    result = birthdayCakeCandles(n, ar)
    print(result)