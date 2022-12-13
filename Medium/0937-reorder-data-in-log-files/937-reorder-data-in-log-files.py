class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, contents = [], []
        
        for i in logs:
            ele = i.split()
            first, rest = ele[0], " ".join(ele[1:])
            
            if rest[0].isdigit():
                digits.append(i)
            else:
                contents.append((rest, first))
            
        contents.sort()
        ans = [x[1] + " " + x[0] for x in contents]
        
        return ans + digits
         