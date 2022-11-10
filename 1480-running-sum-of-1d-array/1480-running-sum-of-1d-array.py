class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in range(len(nums)):
            nums1.append(sum(nums[:i+1]))
        
        return nums1