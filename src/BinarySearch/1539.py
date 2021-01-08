class Solution(object):
    def bsearch(self, arr, val):
        low, high = 0, len(arr) - 1
        while (low <= high):
            mid = (high +low) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def findKthPositive(self, arr, k):
        val = 1
        while k != 0:
            if self.bsearch(arr, val) == -1:
                k -= 1
                if k == 0:
                    return val
            val += 1
        return val
