from Fib import Fib

class FibCount(Fib):
    def __init__(self):
        super().__init__()
        self.call_count = 0

    def fibonacci(self, n):
        self.call_count += 1
        return super().fibonacci(n)
