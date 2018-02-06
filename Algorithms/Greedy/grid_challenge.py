# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:22:25 2018

@author: joseph.chen

https://www.hackerrank.com/challenges/grid-challenge/problem
"""

def gridChallenge(grid):
    # sort each row
    sort_grid = []
    for row in grid:
        row_lst = [e for e in row]
        row_lst.sort()
        sort_grid.append("".join(row_lst))
        
    # now check whether each column has been sorted
    n_row, n_col = len(sort_grid), len(sort_grid[0])
    for n in range(n_col):
        col_lst = []
        for m in range(n_row):
            col_lst.append(sort_grid[m][n])
        sort_col_lst = sorted(col_lst)
        if sort_col_lst!=col_lst:
            return "NO"
    return "YES"
        
        
          
if __name__ == "__main__":
    n = 5
    grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]   
    result = gridChallenge(grid)
    print(result)
    


#if __name__ == "__main__":
#    t = int(input().strip())
#    for test in range(t):
#        n = int(input().strip())
#        grid = []
#        grid_i = 0
#        for grid_i in range(n):
#           grid_t = str(input().strip())
#           grid.append(grid_t)
#        result = gridChallenge(grid)
#        print(result)
