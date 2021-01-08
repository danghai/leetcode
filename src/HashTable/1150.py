class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        dict_t = Counter(nums)
        return dict_t[target] > len(nums) / 2
