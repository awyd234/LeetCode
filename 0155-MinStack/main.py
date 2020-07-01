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


if __name__ == '__main__':
    input1 = (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
              [[], [-2], [0], [-3], [], [], [], []],
              [None, None, None, None, -3, None, 0, -2])
    solution = None
    for index, each_op in enumerate(input1[0]):
        if each_op == "MinStack":
            solution = MinStack()
        else:
            assert getattr(solution, each_op)(*input1[1][index]) == input1[2][index]
