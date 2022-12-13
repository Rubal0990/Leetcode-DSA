class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res