class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 0:
                # item is on right side
                # 1 1 2 2 3 3 4 5 5
                if nums[mid] == nums[mid+1]:
                    low = mid + 2
                else:
                # item is on left side
                # 1 1 2 3 3 4 4 5 5
                    high = mid
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid
        return nums[low]
