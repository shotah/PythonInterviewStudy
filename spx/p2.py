# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# What is the minimum number of minutes for all trucks to finish
# 1 minute per garbage type
# plus travel time.


def solution(travel, types):
    collections = {
        'P': {},
        'G': {},
        'M': {}
    }
    # Build hash of garabage pickups and locations to calculate times
    for idx, pickup in enumerate(types):
        for c_type in collections.keys():
            if c_type in pickup:
                if travel[idx] in collections[c_type]:
                    collections[c_type][travel[idx]] += pickup.count(c_type)
                else:
                    collections[c_type][travel[idx]] = pickup.count(c_type)
    # Calculate Times 
    truck_time = []
    for c_type in collections.keys():
        one_way_time = 0
        garbage_time = 0
        t_time = 0
        for idx, time in enumerate(travel):
            t_time += time
            g_time = collections[c_type].get(time, 0)
            one_way_time = t_time if g_time else 0
            garbage_time += g_time
        truck_time.append(one_way_time*2 + garbage_time)
    return max(truck_time)

travel = [2,5]
types = ["PGP", "M"]

s = solution(travel, types)
# s = find_time_for_slowest_truck(types)
print(s)
