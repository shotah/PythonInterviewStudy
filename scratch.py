# t = [1,1,2,2,3,3]
# r = set(t)
# for i, v in enumerate(r):
#   print(i, v)


# classes = [[1,2],[3,5],[2,2]]
# def percentages(a):
#   return [a[0]/a[1], a]

# def over_fifty(a):
#   return a > 0.5
# avgs_arr = list(map(percentages, classes))
# avgs_arr.sort()
# print(
#   avgs_arr
# )

# import re

# s = "1-(2+3-(42+(5-(1-(2+4-(5+6))))))"
# print(
#   re.findall("(\d+|\+|\-)", s)
# )

# liste = ['a', 'b', 'c']
# value, = liste[3:5] or (None,)
# print(value)  # returns a
# import re
# from itertools import permutations, product

# liste = ['a', 'b', 'c']
# liste.append('0')
# a = "111111111111111111111110011111"
# r = [m.start() for m in re.finditer(pattern='0', string=a)]
# per = list(product(["0","1"],repeat=len(r)))
# print(per)
# result = {}
# for p in per:
#     t = list(a)
#     for i, n in enumerate(p):
#       t[r[i]] = n
#     t = "".join(t)
#     result[t] = True
# print(result)

# for i, n in enumerate(liste):

print(
  ["stuff"] * 3
)
