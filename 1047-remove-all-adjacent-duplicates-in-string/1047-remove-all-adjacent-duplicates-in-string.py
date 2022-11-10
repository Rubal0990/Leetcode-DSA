class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2:
            return s

        stack1 = []
        i = 0

        while i < len(s):
            if stack1 == []:
                    stack1.append(s[i])
            else:
                if stack1[-1] != s[i]:
                        stack1.append(s[i])
                else:
                    stack1.pop()

            i += 1

        return "".join(stack1)