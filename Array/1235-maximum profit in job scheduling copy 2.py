import json
class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

class Solution:
    def __find_last_non_conflicting_job(self, jobs, n):
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid].end <= jobs[n].start:
                low = mid + 1
            else:
                return mid -1
        return -1
    
    def __find_max_profit(self, jobs):
        if not jobs: return 0

        jobs.sort(key=lambda x: x.end)
        n = len(jobs)
        max_profit = [None] * n
        max_profit[0] = jobs[0].profit

        for i in range(1, n):
            index = self.__find_last_non_conflicting_job(jobs, i)
            incl = jobs[i].profit
            if index != -1:
                incl += max(incl, max_profit[i-1])
            max_profit[i] = max(incl, max_profit[i-1])
        return max_profit[n-1]

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x.start)
        return self.__find_max_profit(jobs)

startTime =[1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(
    Solution().jobScheduling(startTime, endTime, profit)
)
