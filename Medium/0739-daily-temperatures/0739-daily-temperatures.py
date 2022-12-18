class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [-1 for _ in range(71)]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            j = [x for x in arr[t-30+1:] if x > -1]
            
            if len(j) == 0:
                res[i] = 0
            else:
                res[i] = min(j)-i
            
            arr[t-30] = i

        return res