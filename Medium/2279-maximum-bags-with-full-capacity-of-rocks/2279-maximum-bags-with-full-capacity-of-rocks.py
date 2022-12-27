class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        comb = sorted(list(zip(capacity, rocks)), key = lambda x: x[0] - x[1])
        res = 0
        
        for cap, rock in comb:
            diff = cap - rock
            if diff == 0:
                res += 1
                
            elif diff > 0:
                if diff <= additionalRocks:
                    additionalRocks -= diff
                    res += 1
                else:
                    break
        
        return res