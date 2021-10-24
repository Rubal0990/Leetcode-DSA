class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res, num = "", columnNumber
        
        while num:
            res += chr((num - 1) % 26 + ord('A'))
            num = (num - 1)//26
            
        return res[::-1]