# return the string true if any two numbers can be multiplied so that the answer is greater than double the sum of all the elements in the array

# def SumMultiplier(arr):
#     # sum all nums in array to have a goal value
#     goal = sum(arr)
#     arr.sort()
#     if arr[-1] * arr[-2] > sum(arr): 
#     # Walk through array with index and number
#     for i, n in enumerate(arr):
#         # return false if we get to the end of the Array
#         if i == len(arr) -1:
#             return False
#         # multiply number by next number to see if its greater than goal
#         if n * arr[i+1] > goal:
#             return True
#     # if we ended up here we did something wrong and it must be false
#     return False

def SumMultiplier(arr):
    arr.sort()
    if arr[-1] * arr[-2] > sum(arr):
        return True
    return False

# keep this function call here
arr = [2, 2, 2, 2, 4, 1]
print(SumMultiplier(arr))
