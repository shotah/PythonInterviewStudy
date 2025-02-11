class Solution:
    def classes_averages_array(self, classes):
        arr = []
        for passes, total in classes:
            val = passes/total
            arr += [str(val)]
        arr.sort()
        return arr

    def classes_averages(self, classes, extraStudents):
        extra_score = 1/extraStudents
        scores = self.classes_averages_array(classes)
        for idx, score in enumerate(scores):
            print(f"working on {score} of index {idx}")
            while scores[idx -1] and score > scores[idx -1] and extraStudents > 0:
                previous_score = scores[idx -1]
                print(f"adding: {extra_score} to {previous_score}")
                extraStudents -= 1
                scores[idx -1] = str(float(previous_score) + float(extra_score))
        return scores

    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        modified_scores = self.classes_averages(classes, extraStudents)
        score_sum = 0
        for score in modified_scores:
            score_sum += float(score)
        return round(score_sum/len(modified_scores), 5)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
# expected: 0.53485
# got: 0.51548
# new got: 0.52083
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(Solution().maxAverageRatio(classes=classes, extraStudents=extraStudents))
