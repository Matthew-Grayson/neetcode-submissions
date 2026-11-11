# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list into two halves
        # (find mid point using slow fast pointers)
        # reverse 2nd half
        # merge in turn

        list1 = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        prev = None
    
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        list2 = prev

        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2
 