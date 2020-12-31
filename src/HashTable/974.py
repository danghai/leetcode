"""
We can prove this one by math.
A % k = x --> A = n1k + x
B % k = x --> B = n2k + x
(A-B) = n1k + x - n2k - x = (n1-n2)*k
It means (A-B) % k = 0
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dict_t = collections.defaultdict(int)
        dict_t[0] = 1
        ans = 0
        running_sum = 0
        for num in A:
            running_sum += num
            ans += dict_t[running_sum % K]
            dict_t[running_sum % K] += 1
        return ans
