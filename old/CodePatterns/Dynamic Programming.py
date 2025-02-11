# https://emre.me/algorithms/dynamic-programming/

# Dynamic programming is all about breaking down an 
# optimization problem into simpler sub-problems, 
# and storing the solution to each sub-problem so 
# that each sub-problem is solved only once.

# Memoization
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
      
memo = {0: 0, 1: 1}
def fibonacci_memoization(n):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]
s = fibonacci_memoization(10)
print(s)

# Tabulation
def fibonacci_tabulation(n):
    if n == 0:
        return n

	# pre-initialize array
    f = [0] * (n + 1)
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
