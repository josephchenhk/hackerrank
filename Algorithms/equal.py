# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:12:43 2018

@author: joseph.chen


http://massivealgorithms.blogspot.hk/2015/01/hackerrank-equal.html

Christy has to equalize the number of chocolates for all the coworkers. The only action she can make at every operation is to increase the count of every others' chocolate by 1,2 or 5 except one of them. This is equivalent to saying, christy can take away the chocolates of one coworker by 1, 2 or 5 while keeping others' chocolate untouched.
Let's consider decreasing a coworker's chocolate as an operation. To minimize the number of operations, we should try to make the number of chocolates of every coworker equal to the minimum one in the group(min). We have to decrease the number of chocolates the ith person A[i] by (A[i] - min). Let this value be x. For this you may consider Coin change algorithms.
we now follow a greedy algorithm so number of operations required is minimum. This can be done in k operations.

k = x/5 +(x%5)/2 + (x%5)%2 

Let f(min) be sum of operations performed over all coworkers to reduce each of their chocolates to min.
However, sometimes f(min) might not always give the correct answer. It can also be a case when

f(min) > f(min-1)

but it is safe to assume that

f(min) < f(min-5)

as f(min-5) takes N operations more than f(min) where N is the number of coworkers.
"""

def equal(arr):
    # Complete this function
    arr.sort()
    min_value = arr[0]
    # f(min)
    fmin = 0
    for a in arr:
        x = a - min_value
        k = x//5 + (x%5)//2 + (x%5)%2
        fmin += k
    # f(min-1)
    fmin1 = 0
    for a in arr:
        x = a - (min_value-1)
        k = x//5 + (x%5)//2 + (x%5)%2
        fmin1 += k  
    # f(min-2)
    fmin2 = 0
    for a in arr:
        x = a - (min_value-2)
        k = x//5 + (x%5)//2 + (x%5)%2
        fmin2 += k   
    # f(min-3)
    fmin3 = 0
    for a in arr:
        x = a - (min_value-3)
        k = x//5 + (x%5)//2 + (x%5)%2
        fmin3 += k 
    # f(min-4)
    fmin4 = 0
    for a in arr:
        x = a - (min_value-4)
        k = x//5 + (x%5)//2 + (x%5)%2
        fmin4 += k 
    return min([fmin, fmin1, fmin2, fmin3, fmin4])
        


if __name__=="__main__":
    n = 4
    #arr = [2, 2, 3, 7]
    arr = [3,7,7,7]
    result = equal(arr)
    print(result)