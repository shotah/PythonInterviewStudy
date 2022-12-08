def solution(a):
    if not a: return 0
    result = {}
    s = set(a)
    for idx, val in enumerate(s):
      result[idx] = list(s)[val]
    return len(result) -1


a = [1, 4, -1, 3, 2]
# expected 4
a =  [2,-1,1,0,0,0]
# expected 3
s = solution(a)
print(s)

