class Solution:
    def percentages(self, a):
        return [str(a[0]/a[1]), a]
    
    def score(self, modified_scores):
        score_sum = 0
        for score, _ in modified_scores:
            score_sum += float(score)
        return round(score_sum/len(modified_scores), 5)

    def classes_averages(self, classes, extraStudents):
        scores = list(map(self.percentages, classes))
        scores.sort()
        print(f"sorted scores: {scores}")
        for idx, score in enumerate(scores):
            print(f"working on {score} of index {idx}")
            while scores[idx -1][0] and score[0] > scores[idx -1][0] and extraStudents > 0:
                extraStudents -= 1
                scores[idx -1][0] = str((scores[idx -1][1][0]+1)/(scores[idx -1][1][1]+1))
                scores[idx -1][1] = [scores[idx -1][1][0]+1,scores[idx -1][1][1]+1]
        print(f"modified scores: {scores}")
        return scores

    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        modified_scores = self.classes_averages(classes, extraStudents)
        return self.score(modified_scores)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
# expected: 0.53485
# got: 0.51548
# new got: 0.52083
# new new score: 0.52197
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(Solution().maxAverageRatio(classes=classes, extraStudents=extraStudents))
