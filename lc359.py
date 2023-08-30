class Logger:

    def __init__(self):
        self.log = {}

        
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log or timestamp - self.log[message] >= 10:
            self.log[message] = timestamp
            return True
        else:
            return False
        



        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)