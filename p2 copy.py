# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# What is the minimum number of minutes for all trucks to finish
# 1 minute per garbage type
# plus travel time.

# outside the box? add all types? get the most of one letter? then calculate that.
def find_time_for_slowest_truck(types):
    all_garbage = "".join(types)
    collection = {}
    for g in all_garbage:
        if g in collection:
            collection[g] +=1
        else:
            collection[g] = 1
    most_garabage = max(collection, key=collection.get)  
    return collection[most_garabage]

def solution(travel, types):
    collection_time = find_time_for_slowest_truck(types)
    travel_time = sum(travel)
    return collection_time + travel_time

travel = [2,5]
types = ["PGP", "M"]

s = solution(travel, types)
# s = find_time_for_slowest_truck(types)
print(s)
