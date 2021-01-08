class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy = Counter(candyType)
        return min(len(candyType) // 2, len(candy))
