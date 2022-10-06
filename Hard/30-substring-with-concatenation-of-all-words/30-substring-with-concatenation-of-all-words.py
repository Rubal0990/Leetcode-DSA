class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt, res, m, n = Counter(words), [], len(words), len(words[0])
        
        for i in range(len(s) - m * n + 1):
            curCnt = defaultdict(int)
            
            for j in range(m):
                a = s[i + j * n: i + (j + 1) * n]
                if not cnt[a] or curCnt[a] + 1 > cnt[a]: 
                    break
                
                curCnt[a] += 1
            else:
                res.append(i)
        
        return res