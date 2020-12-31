class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dict_t = collections.defaultdict(int)
        dict_t[0] = 1
        running_sum = 0
        for num in nums:
            running_sum += num
            ans += dict_t[running_sum - k]
            dict_t[running_sum] += 1
        return ans
