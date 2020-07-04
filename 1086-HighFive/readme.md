# 1086. High Five

link: [https://leetcode.com/problems/high-five/](https://leetcode.com/problems/high-five/)

## Difficulty
Easy

## 题目

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

 
Example 1:
```
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
```
 

Note:
- 1 <= items.length <= 1000
- items[i].length == 2
- The IDs of the students is between 1 to 1000
- The score of the students is between 1 to 100
- For each student, there are at least 5 scores

Accepted
27,351

Submissions
34,543

## 问题描述
输出每个学生最高的5个分值的取整平均数

## 题目分析
没什么难度，按题目意思一步步来就行，不过这个运行速度有些太慢了，猜测和开内存有关

## 代码实现

```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
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
            
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		108 ms	| 14 MB		| python3|

Runtime: 108 ms, faster than 15.55% of Python3 online submissions for High Five.

Memory Usage: 14 MB, less than 80.66% of Python3 online submissions for High Five.