class Solution:
    def jobScheduling(self, st: List[int], et: List[int], pr: List[int]) -> int:
        jobs, n = sorted(zip(st, et, pr)), len(st)
        dp = [0] * (n + 1)
        
        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])
            dp[i] = max(jobs[i][2] + dp[k], dp[i+1])
            
        return dp[0]