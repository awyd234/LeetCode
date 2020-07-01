# 155. Min Stack

link: [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/)

## Difficulty
Easy

## 题目

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
 

**Example 1:**
```markdown
**Input**
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

**Output**
[null,null,null,null,-3,null,0,-2]

**Explanation**
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- Methods pop, top and getMin operations will always be called on non-empty stacks.

Accepted
551,171
Submissions
1,251,970

## 问题描述
自己构造栈，并实现取最小值的方法

## 题目分析
就是用list模拟数组，我这个方法


## 代码实现

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []

    def push(self, x: int) -> None:
        if not self.data:
            self.min_data.append(x)
        else:
            if self.min_data[-1] <= x:
                self.min_data.append(self.min_data[-1])
            else:
                self.min_data.append(x)
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## 运行结果

| Time Submitted | Status                                   | Runtime | Memory  | Language |
| -------------- | ---------------------------------------- | ------- | -------- | -------- |
| a few seconds ago |	Accepted	| 		64 ms	| 17.5 MB		| python3|

Runtime: 64 ms, faster than 70.15% of Python3 online submissions for Min Stack.
Memory Usage: 17.5 MB, less than 59.45% of Python3 online submissions for Min Stack.