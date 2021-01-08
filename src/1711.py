class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        dict_t = collections.defaultdict(int)
        for num in deliciousness:
            for j in range(22):
                if 2**j - num in dict_t:
                    ans += dict_t[2**j - num]
            dict_t[num] += 1
        return ans % (10**9 + 7)
