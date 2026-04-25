class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            largest = stones[0]
            heappop(stones)
            nearly_largest = stones[0]
            heappop(stones)
            print(f"largest {largest}")
            print(f"nearly largest {nearly_largest}")
            if largest != nearly_largest:
                heappush(stones, largest - nearly_largest)
        return -stones[0] if stones else 0
                