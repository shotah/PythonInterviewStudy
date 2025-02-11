class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        result = {}
        for num in arr: 
            if not num in result:
                result[num] = 1
            else:
                result[num] += 1
        test_arr = []
        for val in result.values():
            if val in test_arr :
                return False
            test_arr.append(val)
        return True

arr = [1,2,2,1,1,3]
arr = [1,2]
print(
  Solution().uniqueOccurrences(arr)
)
