# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_node = ListNode(0)
        tail = output_node
        while l1 and l2:
            this_node = ListNode(0)
            this_node.next = None
            if l1.val <= l2.val:
                this_node.val = l1.val
                l1 = l1.next
            else:
                this_node.val = l2.val
                l2 = l2.next
            tail.next = this_node
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return output_node.next
