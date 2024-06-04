class Solution:
    def __highest_profit(self, jobs: list[list[int]], index: int, memo: dict) -> int:
        # guard for zero length jobs
        if index == len(jobs): return 0
        
        # memoized functions, return if already solved.
        if index in memo: return memo[index]

        # get job a so we can compare for next job.
        a_job_profit = self.__highest_profit(jobs, index + 1, memo)
        
        # set b job index incase it is not found.
        b_job_index = None
        
        # move through rest of the indexes and see if current job is greater than next job.
        for cur_index in range(index + 1, len(jobs)):
            # looks at end time of index to make sure its less than start time of current index.
            if jobs[index][1] <= jobs[cur_index][0]:
                # Set b index to current index.
                b_job_index = cur_index
                break
        
        # if b job index doesn't exist, then just take current index profit.
        if not b_job_index:
            b_job_profit = jobs[index][2]
        else:
            # set b job to be current job plus the recursion of job b
            b_job_profit = jobs[index][2] + self.__highest_profit(jobs, b_job_index, memo)
        
        # memoize current comparison so it doesn't run again.
        memo[index] = max(a_job_profit, b_job_profit)
        # return highest value job from memo.
        return memo[index]

    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        # break jobs up into their own lists.
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        # sort in order of start time.
        jobs.sort(key=lambda x: x[0])
        # run recursion
        return self.__highest_profit(jobs, 0, {})


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print(Solution().jobScheduling(startTime, endTime, profit))
