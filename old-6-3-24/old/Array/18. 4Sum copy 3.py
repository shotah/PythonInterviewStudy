class Solution:
    def fourSum(self, arr, s):
        if len(arr) <= 3:
            return []
        sums = {}
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] not in sums:
                    sums[arr[i] + arr[j]] = [[i, j]]
                else:
                    sums[arr[i] + arr[j]].append([i, j])
        ans = set()
        checked = set()
        for x in sums:
            if s - x in sums and x not in checked:
                for elements in sums[x]:  # pair
                    [i1, j1] = elements[0], elements[1]
                    for items in sums[s - x]:
                        if i1 not in items and j1 not in items:
                            possible = sorted(
                                [arr[i1], arr[j1], arr[items[0]], arr[items[1]]]
                            )
                            ans.add(tuple(possible))
            checked.add(s - x)
        return sorted(ans)


nums = [1, 0, -1, 0, -2, 2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# nums = [2,2,2,2,2]
# target = 8
# Output: [[2,2,2,2]]
print(nums)
s = Solution().fourSum(nums, target)
print(s)
