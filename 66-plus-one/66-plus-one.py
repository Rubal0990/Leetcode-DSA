class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        m = map(str, digits)
        s = "".join(m)
        n = str(int(s) + 1)
        return list(n)