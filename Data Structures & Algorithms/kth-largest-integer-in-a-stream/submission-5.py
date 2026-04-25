class KthLargest:
    # from heapq import heapify, heappush, heappop
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # how to append 
        while len(self.nums) > k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) <= self.k:
            return self.nums[0]
        else:
            heapq.heappop(self.nums)
            return self.nums[0]