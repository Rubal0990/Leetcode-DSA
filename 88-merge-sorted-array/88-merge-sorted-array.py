class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        ans = m + n - 1
		
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[ans] = nums1[left]
                ans -= 1
                left -= 1
            else:
                nums1[ans] = nums2[right]
                ans -= 1
                right -= 1
				
        while right >= 0:
            nums1[ans] = nums2[right]
            ans -= 1
            right -= 1
        