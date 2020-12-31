class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dict_t = {}
        dict_t[0] = -1
        running_sum = 0
        ans = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - k in dict_t:
                ans = max(ans, i - dict_t[running_sum-k])
            if not running_sum in dict_t:
                dict_t[running_sum] = i
        return ans
