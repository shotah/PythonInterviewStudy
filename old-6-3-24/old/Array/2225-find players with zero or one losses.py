class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = set()
        losses = {}
        winners = []
        one_losses = []
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            if not losses.get(match[1]):
                losses[match[1]] = 1
            else:
                losses[match[1]] += 1
        for player in sorted(players):
            if player not in losses:
                winners.append(player)
            if losses.get(player, 0) == 1:
                one_losses.append(player)
        return [winners, one_losses]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# [[1,2,10],[4,5,7,8]]

# matches = [[2,3],[1,3],[5,4],[6,4]]
# [[1,2,5,6],[]]

print(
    Solution().findWinners(matches)
)
