class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile(r'[-+]?[0-9]+')
        s = s.strip()
        word_list = pattern.findall(s)
        
        if word_list:
            value = word_list[0]
            if s.startswith(value):
                value = int(value)
                if value > 2**(31)-1:
                    return 2**(31)-1
                
                elif value < -2**(31):
                    return -2**(31)
                
                else:
                    return value
            
            else:
                return 0
        
        else:
            return 0