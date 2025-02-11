# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(a):
    if not a:
        return 0
    r = {}
    for c in a:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    result = [k for k, v in r.items() if v < 2]
    return result[0] if result else 0


a = [9, 3, 9, 3, 9, 7, 9]


s = solution(a)
print(s)
