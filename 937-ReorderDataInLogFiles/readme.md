# 937. Reorder Data in Log Files

link: [https://leetcode.com/problems/reorder-data-in-log-files/](https://leetcode.com/problems/reorder-data-in-log-files/)

## Difficulty
Easy

## 题目

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

- Each word after the identifier will consist only of lowercase letters, or;
- Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:
```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```

Constraints:
- 0 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- logs[i] is guaranteed to have an identifier, and a word after the identifier.

Accepted
91,165
Submissions
170,129

## 问题描述
按指定规则，排序list，数字结尾的在后，按顺序来，字母结尾的在前，按字母顺序

## 题目分析
这题本身比较简单，不过这个的实现方式很新颖，通过构建tuple以及内部排序方法，这种方式值得学习


## 代码实现

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def order_func(log):
            log_id, log_data = log.split(' ', 1)
            return (0, log_data, log_id) if log_data[0].isalpha() else (1, )
        return sorted(logs, key=order_func)
```



## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		36 ms	| 13.8 MB		| python3|

Runtime: 36 ms, faster than 57.18% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Reorder Data in Log Files.