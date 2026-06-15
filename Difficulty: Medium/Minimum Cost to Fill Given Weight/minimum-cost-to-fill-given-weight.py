
class Solution:
    def minimumCost(self, cost, w):
        # dp[j] will store the minimum cost to buy exactly j kg of oranges
        dp = [float('inf')] * (w + 1)
        
        # Base case: 0 kg costs 0
        dp[0] = 0
        
        n = len(cost)
        
        # Traverse through all packet weights (1-indexed)
        for i in range(n):
            packet_weight = i + 1
            packet_cost = cost[i]
            
            # Skip if the packet of this weight is unavailable
            if packet_cost == -1:
                continue
                
            # Update dp array for all weights from packet_weight to w
            for j in range(packet_weight, w + 1):
                if dp[j - packet_weight] != float('inf'):
                    dp[j] = min(dp[j], dp[j - packet_weight] + packet_cost)
                    
        # If dp[w] is still infinity, it means exact weight w cannot be formed
        return dp[w] if dp[w] != float('inf') else -1