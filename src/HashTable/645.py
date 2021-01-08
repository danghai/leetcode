class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        for num in counter:
            if counter[num] == 2:
                val1 = num
        len_t = len(nums) + 1
        total = sum(list(range(1, len_t)))
        val2 = total - sum(nums) + val1
        return [val1, val2]
