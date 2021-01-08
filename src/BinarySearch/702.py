class Solution(object):
    def search(self, reader, target):
        size = 1
        index = 0
        while reader.get(index) < target:
            index = size
            size = 2*size
        low, high = 0, size
        while low <= high:
            mid = low + (high - low) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
