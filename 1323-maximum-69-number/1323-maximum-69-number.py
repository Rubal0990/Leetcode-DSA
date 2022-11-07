class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        
        for i in reversed(range(4)):
            d, n = divmod(n, 10**i)
            if d == 6: return num + 3*10**i
        
        return num
        