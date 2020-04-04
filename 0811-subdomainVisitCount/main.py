class Solution:
    def subdomainVisits(self, cpdomains):
        count_dict = {}
        for each_item in cpdomains:
            count, address_origin = each_item.split(' ')
            address_list = address_origin.split('.')
            for each_index in range(len(address_list)):
                this_address = '.'.join(address_list[each_index:])
                if count_dict.get(this_address) is None:
                    count_dict[this_address] = 0
                count_dict[this_address] += int(count)
        return ['%d %s' % (count, sub_domain) for sub_domain, count in count_dict.items()]


if __name__ == '__main__':
    solution = Solution()
    this_input1 = ["9001 discuss.leetcode.com"]
    assert sorted(solution.subdomainVisits(this_input1)) == sorted(
        ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"])
