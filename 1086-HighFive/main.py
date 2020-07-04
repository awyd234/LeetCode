class Solution:
    def highFive(self, items) -> list:
        all_scores_dict = {}
        result_list = []
        for each_data in items:
            student_id, score = each_data
            if student_id not in all_scores_dict:
                all_scores_dict[student_id] = []
            all_scores_dict[student_id].append(score)
        for each_student_id, score_list in all_scores_dict.items():
            score_list = sorted(score_list, reverse=True)
            result_list.append([each_student_id, sum(score_list[:5]) // 5])
        return result_list


if __name__ == '__main__':
    solution = Solution()
    this_input = list()
    this_input.append(
        [[[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]],
         [[1, 87], [2, 88]]])
    for each_value in this_input:
        assert solution.highFive(each_value[0]) == each_value[1]
