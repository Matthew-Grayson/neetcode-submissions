# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        dummy = ListNode(None)
        total = dummy

        while l1 and l2:
            val = l1.val + l2.val
            
            if carry:
                val += 1
            carry = val >= 10

            if carry:
                val = val % 10
            
            total.next = ListNode(val)

            l1 = l1.next
            l2 = l2.next
            total = total.next

        remaining = l1 or l2
        while remaining:
            val = remaining.val
            if carry:
                val += 1
            carry = val >= 10

            if carry:
                val = val % 10
            
            total.next = ListNode(val)
            total = total.next
            remaining = remaining.next
        
        if carry:
            total.next = ListNode(1)
        
        return dummy.next