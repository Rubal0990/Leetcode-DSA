class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        
        for i in magazine:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        for char in ransomNote:
            if char not in dict1:
                return False
            if dict1[char] == 0:
                return False
            dict1[char] -= 1
        return True