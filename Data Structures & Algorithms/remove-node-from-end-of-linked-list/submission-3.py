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

        if not head.next:
            return None

        left = head
        right = head
        while n > 0:
            right = right.next
            n -= 1

        if right is None and left == head:
            return head.next
            
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next or None
    
        return head
        