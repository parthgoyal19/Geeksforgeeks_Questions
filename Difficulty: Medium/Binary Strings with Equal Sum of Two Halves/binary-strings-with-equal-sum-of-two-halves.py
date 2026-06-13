
class Solution:
    def computeValue(self, n):
        MOD = 10**9 + 7
        
        # Calculate (2n)! and (n!)
        num = 1
        den = 1
        
        # Compute factorial values up to 2n
        # We can compute both needed parts in a single loop
        for i in range(1, n + 1):
            den = (den * i) % MOD
            
        # (n!)^2 % MOD
        den = (den * den) % MOD
        
        for i in range(1, 2 * n + 1):
            num = (num * i) % MOD
            
        # Compute modular inverse of den using Fermat's Little Theorem
        # den^(MOD-2) % MOD
        inv_den = pow(den, MOD - 2, MOD)
        
        # Result is (num * inv_den) % MOD
        return (num * inv_den) % MOD