class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        
        for i in position:    
            if i%2 != 0:
                oddCount += 1
            else:
                evenCount += 1
                
        if oddCount == len(position) or evenCount == len(position):
            return 0
        else:
            return min(evenCount, oddCount)