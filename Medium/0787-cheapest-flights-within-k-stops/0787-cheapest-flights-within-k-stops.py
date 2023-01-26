class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.dst = dst
        self.graph = {key: [] for key in range(n)}
        for flight in flights:
            self.graph[flight[0]].append((flight[1], flight[2]))
        
        self.memo = [[None for _ in range(k+2)] for _ in range(n)]
        
        res = self.dp(src, 0, k+1)
        res = res if res != inf else -1
        return res
    
    def dp(self, cur, price, step):
        if cur == self.dst: return price
        if step == 0: return inf
        
        if self.memo[cur][step]: return self.memo[cur][step]
        
        res = inf
        for item in self.graph[cur]:
            neighbor, cost = item[0], item[1]
            res = min(res, self.dp(neighbor, price, step-1) + cost)
            
        self.memo[cur][step] = res
        return res