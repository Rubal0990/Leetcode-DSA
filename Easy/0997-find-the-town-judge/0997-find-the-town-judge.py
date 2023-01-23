class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        diff_between_beingTrustedBy_and_trusting = defaultdict(int)

        for a,b in trust:
            diff_between_beingTrustedBy_and_trusting[a] -= 1
            diff_between_beingTrustedBy_and_trusting[b] += 1

        for i in range(1, n + 1):
            if diff_between_beingTrustedBy_and_trusting[i] == n-1:
                return i
        
        return -1