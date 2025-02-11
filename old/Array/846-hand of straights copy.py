import copy

class Solution:
    handDict = {}
    def setHandDict(self, hand):
        for idx, card in enumerate(hand):
            self.handDict[idx] = card

    def getCardFromHandDict(self, card):
        for idx, cardFromDict in self.handDict.items():
            if cardFromDict == card:
                return self.handDict.pop(idx)
        return False

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # test if this is even possible
        devisableBySize = len(hand) % groupSize == 0
        if not devisableBySize: return False
        
        # massage the data
        hand.sort()
        self.setHandDict(hand)

        # start loop to validate the order of the cards
        gCount = 1
        nextCard = None
        for idx, card in enumerate(hand):
            # Guard on end of groupSize
            if gCount == groupSize:
                gCount = 1
                continue

            # get the next card and validate it is not false
            nextCard = self.getCardFromHandDict(card=(card+1))
            if not nextCard:
                return False

            # iterate and remove already used values from hand
            gCount += 1
            hand.pop(idx)
            [hand.pop(iidx) for iidx, icard in enumerate(hand) if icard == nextCard]
        return True



# true
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
#true 
hand = [8,10,12]
groupSize = 3
# false
hand = [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11]

groupSize = 10
print(
  Solution().isNStraightHand(hand, groupSize)
)
