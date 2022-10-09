class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ""
        ans = []
        
        for i in digits:
            str1 += str(i)
        
        str1 = str(int(str1) + 1)
        
        for i in str1:
            ans.append(i)
        
        return ans