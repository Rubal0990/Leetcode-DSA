class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        res = mid = 0 

        for word in counter.keys():
            if word[0] == word[1]:
                if counter[word]%2 == 0:
                    res += counter[word] 
                else:
                    res += counter[word] - 1
                
                mid |= counter[word] % 2
            
            elif word[::-1] in counter:
                res += min(counter[word], counter[word[::-1]])
        
        return (res + mid) * 2