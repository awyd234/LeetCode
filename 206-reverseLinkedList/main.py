# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        first_node = ListNode(0)
        first_node.next = head
        tail = head
        while tail.next:
            first_node.next = tail.next
            tail.next = tail.next.next
            first_node.next.next = head
            head = first_node.next
        return first_node.next


def create_list(values):
    if len(values) > 0:
        this_node = ListNode(values[0])
        this_node.next = create_list(values[1:])
    else:
        this_node = None
    return this_node


def traverse_list(nodes_list):
    result = []
    while nodes_list:
        result.append(nodes_list.val)
        nodes_list = nodes_list.next
    return result


if __name__ == '__main__':
    solution = Solution()
    this_input1 = [1, 2, 3, 4, 5]
    list1 = create_list(this_input1)
    assert traverse_list(solution.reverseList(list1)) == reversed(this_input1)
