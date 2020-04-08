class Solution:
    def reorderLogFiles(self, logs):
        def order_func(log):
            log_id, log_data = log.split(' ', 1)
            return (0, log_data, log_id) if log_data[0].isalpha() else (1, )
        return sorted(logs, key=order_func)