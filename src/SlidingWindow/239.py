class Solution(object):
    # Note: Time Limit Exceeded
    def maxSlidingWindow(self, nums, k):
        max_t = max(nums[0:k])
        n = len(nums)
        ret = [max_t]
        for i in range(n-k):
            j = i + k
            if nums[j] >= max_t:
                max_t = nums[j]
            elif nums[i] == max_t:
                max_t = max(nums[i+1:j+1])

            ret.append(max_t)
        return ret
    
    #Deque solution but using default Python array
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 0:
            return nums
        res = []
        dq = []
        for i in range(0,len(nums)):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            if dq and i - k >= dq[0]:
                dq.pop(0)
            dq.append(i)
            if i >= k-1: # i == k-1 is the beginning of a full window
                res.append(nums[dq[0]]) #the biggest number is always the first number in the queue
            #print(dq)
        return res

