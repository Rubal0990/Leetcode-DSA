class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                return nums[i]                