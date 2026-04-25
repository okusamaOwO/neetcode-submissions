class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        import math
        piles = sorted(piles)
        max_banana = piles[-1]
        sum = 0
        for banana_each_pile in piles:
            sum += banana_each_pile
        min_result = math.ceil(sum/h)

        result = max_banana
        while(min_result <= max_banana):
            k = int((min_result + max_banana)/2)
            print(f"this is k {k}")
            print(f"this is min_result {min_result}")
            print(f"this is max banana {max_banana}")
            min_hours = 0
            for pipe in piles:
                min_hours += math.ceil(pipe / k)
            if min_hours > h:
                min_result = k + 1
            elif min_hours <= h:
                max_banana = k - 1
                if result > k:
                    result = k
        return result



        return -1 