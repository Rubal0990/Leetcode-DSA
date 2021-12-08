class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res
    
    def backtrack(self, path, target, indx):
        
        if target == 0:
            self.res.append(path)
            return
        
        if target < 0:
            return
        
        for x in range(indx, len(self.candidates)):
            self.backtrack(path + [self.candidates[x]], target - self.candidates[x], x)