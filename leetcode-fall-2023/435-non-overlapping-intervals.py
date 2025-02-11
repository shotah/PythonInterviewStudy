# class Solution:
#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#         # guard clause
#         if not intervals or len(intervals) == 1:
#             return 0

#         # sorted by end time to maximize meeting times.
#         intervals.sort(key=lambda x: x[1])
#         n = len(intervals)
#         prev = 0
#         count = 1
#         # walk through the rest of the indexes.
#         for i in range(1, n):
#             # since these are sorted by end time we can just check start time to prev end time.
#             if intervals[i][0] >= intervals[prev][1]:
#                 # set previous
#                 prev = i
#                 # set count
#                 count += 1
#         # since we know how many DO NOT OVERLAP, we just need to subtract it from overall length.
#         return n - count


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        intervals.sort(key=lambda i: i[1])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end
        return res


s = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(s.eraseOverlapIntervals(intervals))
