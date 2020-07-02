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
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


if __name__ == '__main__':
    solution = Logger()
    this_input = list()
    this_input.append([1, "foo", True])
    this_input.append([2, "bar", True])
    this_input.append([3, "foo", False])
    this_input.append([8, "bar", False])
    this_input.append([10, "foo", False])
    this_input.append([11, "foo", True])
    for each_value in this_input:
        assert solution.shouldPrintMessage(each_value[0], each_value[1]) == each_value[2]
