# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
# For example, consider array A such that:

# Array A represents numbers on a tape.
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3

# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3

# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(a):
    if not a or len(a) == 1: return 0
    left_sum = sum(a[:1])
    right_sum = sum(a[1:])
    min_sol = abs(left_sum - right_sum)
    for i in range(1, len(a)):
        left_sum += a[i]
        right_sum -= a[i]
        cur_min = abs(left_sum - right_sum)
        min_sol = min(cur_min, min_sol)
    return min_sol
    
    
a = [9, 3, 9, 3, 9, 7, 9]
a = [2]
a = [3, 1, 2, 4, 3]
a = [3000, 1000]

s = solution(a)
print(s)

