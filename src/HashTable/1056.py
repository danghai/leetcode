class Solution:
    def confusingNumber(self, N: int) -> bool:
        confused = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        str_n = str(N)
        ans = ''
        used = 0
        for c in str_n[::-1]:
            if not c in confused:
                return False
            else:
                ans += confused[c]
        ans = int(ans)
        return ans != N
