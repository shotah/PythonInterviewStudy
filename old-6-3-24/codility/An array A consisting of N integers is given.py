# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    """
    If no a or k then return array
    If array and key then rotate array and return array
    """
    if not A or not K: return A
    while K > 0:
      A.insert(0, A.pop())
      K -= 1
    return A


A = [3, 8, 9, 7, 6]
A = []
K = 3

s = solution(A, K)
print(s)
