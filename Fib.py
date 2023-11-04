class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Fib(metaclass=Singleton):
    def __init__(self):
        self.store_val = {0: 0, 1: 1}

    def fibonacci(self, n):
        if n not in self.store_val:
            x, y = 0, 1
            for _ in range(2, n + 1):
                x, y = y, x + y
            self.store_val[n] = y
        return self.store_val[n]
