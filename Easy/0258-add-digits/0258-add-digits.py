class Solution:
    def addDigits(self, num: int) -> int:
            def help(num):
                num = str(num)
                sum1 = 0

                for i in num:
                    sum1 += int(i)
                
                return sum1
            
            while len(str(num)) != 1:
                num = help(num)
            
            return num