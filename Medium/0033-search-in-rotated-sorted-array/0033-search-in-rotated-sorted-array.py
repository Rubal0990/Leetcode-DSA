class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)
    
    def helper(self, arr: List[int], l: int, h: int, key: int):
        if l > h:
            return -1
        
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid

        if arr[l] <= arr[mid]:
            if key >= arr[l] and key <= arr[mid]:
                return self.helper(arr, l, mid-1, key)
            
            return self.helper(arr, mid + 1, h, key)

        if key >= arr[mid] and key <= arr[h]:
            return self.helper(arr, mid + 1, h, key)

        return self.helper(arr, l, mid-1, key)
                    
            