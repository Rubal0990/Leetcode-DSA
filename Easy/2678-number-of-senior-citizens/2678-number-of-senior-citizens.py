class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0

        for item in details:
            age = item[11:13]
            age = "".join(age)
            
            if int(age) > 60:
                cnt += 1
        
        return cnt