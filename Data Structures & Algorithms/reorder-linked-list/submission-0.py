# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        prev = None

        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        
        left, right = head, prev

        while right:
            tempLeft, tempRight = left.next, right.next
            left.next = right
            right.next = tempLeft
            left = left.next
            left = tempLeft
            right = tempRight
