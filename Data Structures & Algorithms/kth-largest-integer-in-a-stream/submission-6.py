class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
    def add(self, val: int) -> int:
        from heapq import heapify, heappop, heappush
        copy_nums = self.nums.copy()
        heapify(copy_nums)
        heappush(copy_nums, -1 * val)
        self.nums.append(-1 * val)
        for i in range(self.k-1):
            print(copy_nums)
            heappop(copy_nums)
        return -1 * heappop(copy_nums)

