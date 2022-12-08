# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

def solution(a):
    if not a: return 1
    a.sort()
    if a[0] != 1: return 1
    for i in range(len(a)):
        try:
            if a[i+1] - a[i] != 1:
                return a[i] + 1
        except:
            return a[i] + 1
    return a[0] -1




a = [9, 3, 9, 3, 9, 7, 9]
a = [2]

s = solution(a)
print(s)
