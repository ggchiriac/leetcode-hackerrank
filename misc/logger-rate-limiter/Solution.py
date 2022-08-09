// https://leetcode.com/problems/logger-rate-limiter

class Logger:

    def __init__(self):
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logger:
            self.logger[message] = timestamp
            return True
        else:
            if timestamp - self.logger[message] >= 10:
                self.logger[message] = timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)