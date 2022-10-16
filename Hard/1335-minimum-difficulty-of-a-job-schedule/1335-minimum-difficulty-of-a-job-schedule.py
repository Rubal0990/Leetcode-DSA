class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def res(pos=0, d=d, mx=0):
            if d==0 and pos!=len(jobDifficulty):
                return math.inf
            
            elif d==0 and pos==len(jobDifficulty):
                return 0
            
            elif d==0 or pos==len(jobDifficulty):
                return math.inf
            
            else:
                return min(res(pos+1, d, max(mx, jobDifficulty[pos])), max(mx, jobDifficulty[pos]) + res(pos+1, d-1, 0))
        
        ret = res()
        return -1 if ret == math.inf else ret
        