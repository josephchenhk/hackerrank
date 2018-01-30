# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:39:11 2018

@author: joseph.chen
"""

#https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/

"""
Recursive
"""
def getWays2(n, c):
		if n<0:
			return 0
		if n == 0:
			return 1
		sum = 0
		for i in range(len(c)):
			target = n - c[i];
			subc = c[i:]
			result = getWays(target, subc);
			sum += result
		return sum
 
"""
Dynamic programing
Recurrence:
    d(4, [1,2,3]) = d(4-1, [1,2,3]) + d(4-2, [2,3]) + d(4-3, [3])
"""
def getWays(n, c, memo={}):
    if n<0:
        return 0
    if n==0:
        return 1
    c_str = ",".join([str(coin) for coin in c])
    if (n,c_str) in memo:
        print("memo[%s,%s]=%s"%(n, c_str, memo[(n,c_str)]))
        return memo[(n,c)]
    
    sum = 0
    for i in range(len(c)):
        target = n - c[i]
        subc = c[i:]
        result = getWays(target, subc, memo)
        if result>0:
            subc_str = ",".join([str(coin) for coin in subc])
            memo[(target,subc_str)] = result
            print("*memo[(%s,%s)]=%s"%(target, subc_str, memo[(target,subc_str)]))
        sum += result
    return sum


if __name__=="__main__":
#    n, m = input().strip().split(' ')
#    n, m = [int(n), int(m)]
#    c = list(map(int, input().strip().split(' ')))
    
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
#    n = 4
#    c = [1,2,3]
#    ways = getWays(n, c)
#    print(ways)
    
    n = 10
    c = [2,5,3,6]
    ways = getWays(n, c)
    print(ways)