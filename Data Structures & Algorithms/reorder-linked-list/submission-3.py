# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # bisect list
        first = head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        # re-merge halves
        while second:
            tempFirst = first.next
            tempSecond = second.next
            first.next = second
            second.next = tempFirst
            first = tempFirst
            second = tempSecond