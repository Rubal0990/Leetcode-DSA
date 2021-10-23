class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        multi = 1
        col = 0
        
        for i in range(len(columnTitle)-1, -1, -1) :
            col = (ord(columnTitle[i])-64) * multi
            multi *= 26
            
        return col