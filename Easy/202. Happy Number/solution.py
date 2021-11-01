class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquare(n)
            
            if n == 1:
                return True        
        return False
    
    def sumOfSquare(self, n: int) -> int:
        out = 0
        
        while n:
            d = n % 10
            d = d ** 2
            out += d
            n = n // 10        
        return out