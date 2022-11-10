class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2:
            return s

        res = []

        for char in s:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)

        return "".join(res)