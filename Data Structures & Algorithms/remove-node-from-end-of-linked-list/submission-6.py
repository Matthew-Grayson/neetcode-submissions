# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge cases:
            # nth node is first node, last node, or only node

        # set left and right pointers n nodes apart
        dummy = ListNode(None, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next
        
        # increment pointers until right = None
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next