RTEMS-Python-Challenge
======================

This is a programming challenge meant to assess basic to intermediate Python programming skills. Read all instructions carefully.

You must do this challenge by yourself. You may discuss the problem or solutions with others, but you may not share code with anyone. You may not use code downloaded from the Internet. You *must* identify any resources that you used to solve this challenge.

You should first **fork** this repository to your own *private* repo. You are expected to work on your repo by making *git-commit* as you work. In the end, you should submit your entire set of all commits as a single **pull request**. In this way, the entire *history* of your programming efforts will be reflected in the commits you made, while the PR will merge all of these to provide a consolidated changeset that we can review.

The Challenge
-------------

The Fibonacci Sequence is the series of numbers like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it.
    • 2 is found by adding the two numbers before it (1+1)
    • 3 is found by adding the two numbers before it (1+2),
    • 5 is (2+3),
    • ……
An implementation is given in the file *fibonacci.py* like this
```Python
def fibonacci(num):
	if num < 2:
		return num
	return fibonacci(num - 1) + fibonacci(num - 2)
```

The runtime performance of this code is terrible, because it recalculates Fibonacci numbers that are already known. 

Your job is to first refactor the given code to an object-oriented style by defining a new `class Fib` that contains the `fibonacci` function with an identical interface as the current version of `fibonacci` except with the `self` argument needed for class member methods. Put your new class in a file *Fib.py* and replace the call to `fibonacci` in `fibonacci.py` with an instantiation of a `Fib` object. While you're at it, you should also replace the use of `getopt` with `argparse` for command line argument processing. Add your own copyright as appropriate to existing or new files.

So far, the functionality of *fibonacci.py* should be the same as before. With this version, take a baseline measurement of the runtime performance, for example:
```
$ time python3 fibonacci.py -n 30
9227465

real  0m2.060s
user  0m2.056s
sys	  0m0.005s
```
Use a value of `n` sufficiently large enough to take at least 1 second.

So far, so good. Now, implement `class FibCount` that inherits from `Fib` and provides the same `fibonacci` interface, but keeps track of how many calls are made to `fibonacci`. Put this class in a file *FibCount.py* and replace the instantiation of the `Fib` object in `fibonacci.py` with an instantiation of a `FibCount` object. Modify the `print` statements so that you get the following output for example:
```
$ python3 fibonacci.py -n 30
The 30th Fibonacci number is 832040
Found by making 2692537 calls
```
Time this call, and keep the timing and call count information for later.

We still haven't changed the runtime performance, in fact we made it marginally worse. Let's fix that by implementing `class FibCache` that inherits from `FibCount` and saves the calculations of Fibonnaci subsequences in a class member variable as a dictionary. Update the dictionary each time a new Fibonacci number is calculated, and use the dictionary to return the results of previously computed numbers.

So how much better is your revised version? 
```
$ time python3 FibCache.py -n 30
[...]

```
You tell me! Include how many calls are saved and the timing results comparing the version using `FibCount` and `FibCache` in the comment on your Pull Request.

Good luck. If you have any questions about this challenge, feel free to ask me. Submit your solution by opening a PR with all your code changes, comments as requested, and anything else you would like to say.

