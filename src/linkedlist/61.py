# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head: return head
        len_t = 1
        curr = head
        while (curr.next):
            len_t += 1
            curr = curr.next
        k = k % len_t
        curr.next = head  # Make circle
        curr = head
        for _ in range(len_t - k - 1):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
