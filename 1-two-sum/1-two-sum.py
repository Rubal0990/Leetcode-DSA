class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        
        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in values:
                return [values[diff], i]
            
            values[ele] = i
        
        return ans