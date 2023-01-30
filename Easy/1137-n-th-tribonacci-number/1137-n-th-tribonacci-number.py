class Solution:
    def tribonacci(self, n: int) -> int:
        Tn = (0, 1, 1, 2, 4, 7)
        if n < 6:
            return Tn[n]

        r = n % 3
        a, b, c = Tn[r + 1], Tn[r + 2], Tn[r + 3]
        for _ in range(r + 7, n, 3):
            a, b, c = a + b + c, a + 2*b + 2*c, 2*a + 3*b + 4*c
        
        return 2*a + 3*b + 4*c
