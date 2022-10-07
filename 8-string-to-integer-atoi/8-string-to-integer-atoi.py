class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        s = s.strip()
        num = 0
        sign = 0    

        for i in range(len(s)):  
            if s[i] in ["+", "-"] and sign == 0 and i == 0:
                if s[i] == "-": 
                    sign += 1 
                else: 
                    continue
        
            elif s[i].isnumeric():
                if ((num > INT_MAX // 10) or (num == INT_MAX // 10 and int(s[i]) > INT_MAX % 10)):
                    return INT_MIN if sign == 1 else INT_MAX
                
                num = num * 10 + int(s[i])
                
            else:
                break
                
        return -num if sign == 1 else num