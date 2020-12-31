class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict_t = {0: 0}
        running_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1

            if running_sum in dict_t:
                ans = max(ans, i - dict_t[running_sum] + 1)
            else:
                dict_t[running_sum] = i+1
        return ans
