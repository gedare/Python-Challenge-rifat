from FibCount import FibCount


class FibCache(FibCount):
    def __init__(self):
        super().__init__()
        self.cache = {0: 0, 1: 1}

    def fibonacci(self, n):
        if n not in self.cache:
            self.cache[n] = super().fibonacci(n)
        return self.cache[n]
