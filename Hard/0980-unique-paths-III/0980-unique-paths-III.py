import sys  
sys.setrecursionlimit(1000000)

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        start = 0
        final = 0
        fi = fj = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    final += 1 << (i*m+j)
                
                if grid[i][j] == 1:
                    start += 1 << (i*m+j)
                    si, sj = i, j
                
                if grid[i][j] == 2:
                    fi, fj = i, j

        cache = {(start,si,sj): 1}
    
        def solve(status, i, j):
            if (status,i,j) in cache: 
                return cache[status,i,j]
            
            res = 0
            now_status = 1 << (i*m + j)
            for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=x<n and 0<=y<m and grid[x][y] != -1:
                    mask = 1 << (x*m+y)
                    if status & mask:
                        res += solve(status ^ now_status, x, y)
            
            cache[status,i,j] = res
            return res
        
        return solve(final, fi, fj)
