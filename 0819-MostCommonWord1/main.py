class Solution:
    def processQueries(self, queries, m: int):
        this_list = list(range(1, m + 1))
        output = []
        for each_query in queries:
            this_index = this_list.index(each_query)
            output.append(this_index)
            tmp = this_list[this_index]
            while this_index > 0:
                this_list[this_index] = this_list[this_index - 1]
                this_index -= 1
            this_list[0] = tmp
        return output


if __name__ == '__main__':
    solution = Solution()
    input1 = ([3,1,2,1], 5, [2,1,2,1] )
    assert solution.processQueries(input1[0], input1[1]) == input1[2]