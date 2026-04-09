import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = collections.Counter(hand)
        sorted_unique_cards = sorted(count.keys())
        

        for card in sorted_unique_cards:

            if count[card] > 0:
                groups_to_make = count[card]

                for i in range(card, card+groupSize):
                    if count[i] < groups_to_make:
                        return False
                    count[i] -= groups_to_make
        return True
