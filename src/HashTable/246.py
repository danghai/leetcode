class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_t = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        ans = ''
        for c in num[::-1]:
            if not c in map_t: return False
            ans += map_t[c]
        return ans == num
