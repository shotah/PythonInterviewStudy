# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# delete any duplicate occurrence and calculate the cost per the chart

def solution(letters, costs):
    arr_letters = list(letters)
    arr_result = []
    for idx, ltr in enumerate(arr_letters):
        if idx > 0 and arr_letters[idx-1] == ltr:
            remove_idx = idx -1 if costs[idx -1] < costs[idx] else idx
            arr_result.append(costs[remove_idx])
    return sum(arr_result)

letters = "abccbd"
costs = [0,1,2,3,4,5]
# (aabbcc, [1,2,1,2,1,2])
# letters = "aabbcc"
# costs = [1,2,1,2,1,2]
letters = "aaaa"
costs = [3, 4, 5, 6]
s = solution(letters, costs)
print(s)
