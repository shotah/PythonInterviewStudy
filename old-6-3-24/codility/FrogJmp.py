# For example, given:

#   X = 10
#   Y = 85
#   D = 30
# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100
from math import ceil

def solution(START, GOAL, DISTANCE):
    if START >= GOAL: return 0
    return ceil((GOAL - START)/DISTANCE)



X = 10
Y = 85
D = 30
s = solution(X,Y,D)
print(s)
