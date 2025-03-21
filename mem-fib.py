from typing import Optional

MEM = {}


def fib(n):
    if n in MEM:
        return MEM[n]
    if n == 0 or n == 1:
        return n
    res = fib(n - 1) + fib(n - 2)
    MEM[n] = res
    return res


print(fib(10))
