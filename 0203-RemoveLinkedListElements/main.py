# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        none_head = ListNode(0, None)
        none_head.next = head
        p = none_head
        while p and p.next:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return none_head.next


def create_list(data_list):
    this_head = ListNode(0, None)
    p = this_head
    for each_data in data_list:
        this_node = ListNode(each_data, None)
        p.next = this_node
        p = p.next
    return this_head.next


def traverse(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[1, 1, 1], 1, []])
    this_input.append([[1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]])
    this_input.append([[], 1, []])
    for each_value in this_input:
        assert traverse(solution.removeElements(create_list(each_value[0]), each_value[1])) == each_value[2]
