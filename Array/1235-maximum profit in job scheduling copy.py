class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        past_end = None
        total_profit = 0
        for i, cur_start in enumerate(startTime):
            if (past_end and past_end <= cur_start) or not past_end:
                print(f"iteration {i}")
                total_profit += profit[i]
                past_end = endTime[i]
        return total_profit

startTime =[1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(
    Solution().jobScheduling(startTime, endTime, profit)
)
