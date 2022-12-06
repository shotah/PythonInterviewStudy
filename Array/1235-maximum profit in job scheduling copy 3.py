from functools import lru_cache

class Solution:
    def __bisect_left(self, a, x, lo=0, hi=None, *, key):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def jobScheduling(self, s: list[int], e: list[int], p: list[int]) -> int:
        jobs =[[s[i], e[i], p[i]]  for i in range(len(s))]
        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= len(jobs) : return 0
            k = self.__bisect_left(a=jobs, x=jobs[i][1], key=lambda j: j[0])
            return max(dfs(i+1), jobs[i][2] + dfs(k))
            
        return dfs(0)

startTime =[1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(
    Solution().jobScheduling(startTime, endTime, profit)
)
