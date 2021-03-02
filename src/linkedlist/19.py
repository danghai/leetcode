# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        count = 0
        while (curr):
            curr = curr.next
            count += 1
        if (n == count):
            head = head.next
            return head
        curr = head
        for i in range(count - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head
