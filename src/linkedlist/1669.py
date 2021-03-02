# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        slow1 = fast1 = list1
        slow2 = fast2 = list2
        for i in range(b+1):
            fast1 = fast1.next
        for i in range(a-1):
            slow1 = slow1.next
        while fast2.next:
            fast2 = fast2.next
        slow1.next = list2
        fast2.next = fast1
        return list1
