# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two-pointers n-nodes apart
        # increment both until second pointer reaches the end
        # have first.next point to first.next.next
        # edge cases
            # n is only node
                # return None
            # n is last node
                # prev.next = None
            # n is first node
                # return head.next
        dummy = ListNode(None, head)
        left = dummy
        right = head
        
        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
    
        return dummy.next
        