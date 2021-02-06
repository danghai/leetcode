class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict_t = Counter(nums)
        ret = 0
        for key, val in dict_t.items():
            if val == 1:   # Unique element
                ret += key
        return ret
