# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointers to find middle node
        # reverse second half of list
        # merge first and second half
        first = head
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev

        while second:
            tempFirst = first.next
            first.next = second
            tempSecond = second.next
            second.next = tempFirst
            first = tempFirst
            second = tempSecond
        
