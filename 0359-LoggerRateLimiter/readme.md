# 359. Logger Rate Limiter

link: [https://leetcode.com/problems/logger-rate-limiter/](https://leetcode.com/problems/logger-rate-limiter/)

## Difficulty
Easy

## 题目

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:
```
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
```

Accepted
90,411
Submissions
128,955

## 问题描述
实现一个日志系统，判断当前语句在前10s内是否已经被打印

## 题目分析
很简单的一个题目，对每个语句记录上一次打印时间即可

## 代码实现

```python
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last_print_ts_dict = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.last_print_ts_dict.get(message) is None:
            self.last_print_ts_dict[message] = timestamp
            return True
        if timestamp - self.last_print_ts_dict.get(message) >= 10:
            self.last_print_ts_dict[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		148 ms	| 19.9 MB		| python3|

Runtime: 148 ms, faster than 88.83% of Python3 online submissions for Logger Rate Limiter.

Memory Usage: 19.9 MB, less than 9.67% of Python3 online submissions for Logger Rate Limiter.