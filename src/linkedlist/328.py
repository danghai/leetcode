# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = curr_odd = ListNode()
        even = curr_even = ListNode()
        count = 0
        while head:
            curr = head
            head = head.next
            if count % 2 == 0:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            else:
                curr_even.next = curr
                curr_even = curr_even.next
            curr.next = None
            count += 1
        curr_odd.next = even.next
        return odd.next
