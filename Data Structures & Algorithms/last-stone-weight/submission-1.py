class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            highest = stones[-1]
            high = stones[-2]
            print(highest, high)
            if highest == high:
                stones.pop()
                stones.pop()
            else: 
                stones.pop()
                stones.pop()
                stones.append(highest-high)
            if not stones:
                return 0
        return stones[0]