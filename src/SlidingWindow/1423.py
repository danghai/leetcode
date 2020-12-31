class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        i = 0
        ans = float('inf')
        sum_t = sum(cardPoints[:size])
        ans = min(ans, sum_t)
        for j in range(size, len(cardPoints)):
            sum_t -= cardPoints[i]
            sum_t += cardPoints[j]
            i += 1
            ans = min(ans, sum_t)
        return sum(cardPoints) - ans

