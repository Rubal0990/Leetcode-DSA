class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat[0]), len(mat)
        if m*n != r*c:
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                res[count//c][count%c] = mat[i][j]
                count += 1
                
        return res