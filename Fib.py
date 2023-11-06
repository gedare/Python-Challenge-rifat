import sys


class Fib:
    def __init__(self):
        self.store_val = {0: 0, 1: 1}
        # sys.setrecursionlimit(60000) # set the limit according to the size of n to avoid RecursionError

    def fibonacci(self, n):
        if n not in self.store_val:
            self.store_val[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.store_val[n]
