#!/usr/bin/env python
# SPDX-License-Identifier: BSD-2-Clause
"""Prints the n'th Fibonacci number"""

# Copyright (C) 2021 Gedare Bloom
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
from FibCache import FibCache
import time

def main():
    "Parse the arguments and print fibonacci number"
    parser = argparse.ArgumentParser(description="Calculate Fibonacci numbers.")
    parser.add_argument('-n', '--number', type=int, help='The n-th Fibonacci number to calculate', required=True)
    args = parser.parse_args()

    fib_cache = FibCache()
    start_time = time.time()
    result = fib_cache.fibonacci(args.number)
    end_time = time.time()

    print(f"The {args.number}th Fibonacci number is {result}")
    print(f"Found by making {fib_cache.call_count} calls")
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()



