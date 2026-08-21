/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{} 
	list3 := dummy

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			list3.Next = list1
			list1 = list1.Next
		} else {
			list3.Next = list2
			list2 = list2.Next
		}
		list3 = list3.Next
	}
	list3.Next = list1
	if list1 == nil {
		list3.Next = list2
	}
   
   return dummy.Next
}
