class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        dict_b = collections.defaultdict(int)
        dict_c = collections.defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                dict_b[secret[i]] += 1

        for i in range(len(guess)):
            if secret[i] != guess[i]:
                dict_c[guess[i]] += 1

        for key, val in dict_b.items():
            if key in dict_c:
                cows += min(val, dict_c[key])

        return str(bulls) + 'A' + str(cows) + 'B'
