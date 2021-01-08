class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dict_t = {}
        for i, num in enumerate(arr):
            dict_t[num] = i
        for piece in pieces:
            if len(piece) == 1:
                if not piece[0] in dict_t: return False
                else: continue
            else:
                for i in range(1, len(piece)):
                    num1, num2 = piece[i-1], piece[i]
                    if not num1 in dict_t or not num2 in dict_t:
                        return False
                    if dict_t[num1] > dict_t[num2] or dict_t[num2] - dict_t[num1] != 1:
                        return False
        return True

# Another way
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []

        for num in arr:
            res += mp.get(num, [])

        return res == arr

