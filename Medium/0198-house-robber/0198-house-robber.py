class Solution:
    def frequencySort(self, s: str) -> str:
        c1, c2 = collections.Counter(s), {}
        ans = []
        
        for k, v in c1.items():
            c2.setdefault(v, []).append(k * v)
        
        for i in range(len(s), -1, -1):
            if i in c2:
                ans.append("".join(c2[i]))
        
        return "".join(ans)