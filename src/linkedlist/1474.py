# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        ret = curr_ret = ListNode(0)
        curr = head
        while curr:
            for i in range(m):
                if curr == None: return ret.next
                curr_ret.next = curr
                curr_ret = curr_ret.next
                curr = curr.next
                curr_ret.next = None
            for i in range(n):
                if curr == None: return ret.next
                curr = curr.next
        return ret.next
