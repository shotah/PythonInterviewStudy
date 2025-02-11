def solution(N):
    binary = format(N, 'b')
    max_gap = 0
    latest_gap = 0
    for n in map(int, binary):
      if n == 0:
        latest_gap += 1
      else:
        max_gap = max(max_gap, latest_gap)
        latest_gap = 0       
    return max_gap
  

n = 1041
n = 32
s = solution(n)
print(s)
