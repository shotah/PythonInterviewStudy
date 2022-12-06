class Solution:
    def classes_averages(self, classes, extraStudents):
        avg = 0
        lowest_class = []
        lowest_score = None
        for passes, total in classes:
            score = passes/total
            if not lowest_score or score < lowest_score:
                lowest_score = score
                lowest_class = [passes, total]
            avg += score
        total_average = avg/len(classes)
        avg -= lowest_score
        bumped_score = (lowest_class[0] + extraStudents) / (lowest_class[1] + extraStudents)
        avg += bumped_score
        total_average = avg/len(classes)
        return total_average

    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        return round(self.classes_averages(classes, extraStudents), 5)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
# expected: 0.53485
# got: 0.51548
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(Solution().maxAverageRatio(classes=classes, extraStudents=extraStudents))
