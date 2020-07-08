from utils import ListNode, build_linked_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        to_add = 0
        result = ListNode(0)
        p = result
        while l1 or l2 or to_add != 0:
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            this_data = l1_val + l2_val + to_add
            to_add = this_data // 10
            this_data = this_data % 10
            p.next = ListNode(this_data)
            p = p.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return result.next


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append([[2, 4, 3, 6], [5, 6, 4], [7, 0, 8, 6]])
    this_input.append([[2, 4, 6, 6], [5, 6, 4], [7, 0, 0, 7]])
    for each_value in this_input:
        l1 = build_linked_list(each_value[0])
        l2 = build_linked_list(each_value[1])
        result = build_linked_list(each_value[2])
        assert solution.addTwoNumbers(l1, l2) == result
