# https://emre.me/coding-patterns/topological-sort/


# How to identify?

# Topological Sort pattern is very useful for finding a linear 
# ordering of elements that have dependencies on each other.

# Scheduling or grouping problems which have dependencies 
# between items are good examples to the problems 
# that can be solved with using this technique.


# Problem: Course Schedule
# LeetCode 207 - Course Schedule [medium]

# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1, 0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1, 0], [0, 1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 
#              you should also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list = []

        if numCourses <= 0:
            return False

        # a. Initialization
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        in_degree = {i: 0 for i in range(numCourses)}  # count of incoming edges

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            in_degree[child] += 1

        # c. Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. Sort
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if sorted_list does not contain all the courses, there is a cyclic dependency between courses
        # scheduling is not possible if there is a cyclic dependency
        return len(sorted_list) == numCourses

# Time Complexity: O(V + E) where V is the total number of courses and E is the total number of prerequisites.

# Space Complexity: O(V + E) since we are storing all of the prerequisites for each course in an adjacency list.
