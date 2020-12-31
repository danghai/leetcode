class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict_t = collections.defaultdict(int)
        for i in range(len(s) - 9):
            dict_t[s[i:i+10]] += 1
        ans = []
        for key, val in dict_t.items():
            if val > 1:
                ans.append(key)
        return ans
