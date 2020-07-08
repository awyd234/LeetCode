# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_bst_method1(data: list):
    if len(data) == 0 or all([_ is None for _ in data]):
        return None
    root_node = TreeNode(val=data[0])
    for each_data in data[1:]:
        if each_data is None:
            continue
        this_node = TreeNode(val=each_data)
        p = root_node
        while p:
            if this_node.val < p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = this_node
                    break
            elif this_node.val > p.val:
                if p.right:
                    p = p.right
                else:
                    p.right = this_node
                    break
    return root_node


def build_linked_list(data: list, none_head=True):
    head = ListNode()
    p = head
    for each_data in data:
        this_node = ListNode(each_data)
        p.next = this_node
        p = p.next
    if none_head:
        return head.next
    else:
        return head


def check_linked_list_equal(l1: ListNode, l2: ListNode):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 is None and l2 is None:
        return True
    else:
        return False
