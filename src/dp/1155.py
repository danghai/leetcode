class Solution(object):
    def numRollsToTarget(self, d, f, target):
        return self.dp(d, f, target, memo={}) % (10**9+7)
    
    def dp(self, d, f, target, memo={}):
        if d == 1 and target <= f: return 1
        if d == 1 and target > f: return 0
        
        max = target - (d - 1)
        if max > f: max = f
            
        res = 0
        for i in range(1, max+1):
            if (d-1, target - i) in memo:
                res += memo.get((d-1, target - i))
                continue
            
            memo[(d-1, target - i)] = self.dp(d-1, f, target - i, memo)
            res += memo.get((d-1, target - i))
        return res

        
        
        
        
