class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        diff = float("inf")
        
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                evaluated = nums[i] + nums[left] + nums[right]
                if evaluated == target:
                    return target
                elif evaluated > target:
                    right -= 1
                    if evaluated - target < diff:
                        diff = evaluated-target
                        ans = evaluated
                else:
                    left += 1
                    if target - evaluated < diff:
                        ans = evaluated
                        diff = target - evaluated
        
        return ans