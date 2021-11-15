class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc", "3":"def", "4":"ghi",
                    "5":"jkl", "6":"mno", "7":"pqrs",
                    "8":"tuv", "9":"wxyz"}
        
        def maker( digit_string ):
            if digit_string == "":
                return []
            
            elif digit_string in mapping:
                return [*mapping[digit_string]]
            
            this_round = mapping[digit_string[0]]
            next_round = maker(digit_string[1:])
            
            return [cur_comb + next_comb for cur_comb in this_round for next_comb in next_round]
        
        return maker(digits)