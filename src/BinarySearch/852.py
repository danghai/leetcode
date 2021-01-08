class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, h = 0, len(A)
        while l < h:
            mid = l + (h - l) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                h = mid
        return l
