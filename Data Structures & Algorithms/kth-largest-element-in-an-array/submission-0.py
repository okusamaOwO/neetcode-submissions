class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if sorting => O(nlogn)
        # hmm, did u meant using a heap map
        from heapq import heapify, heappop, heappush
        new_list = [-num for num in nums]
        heapify(new_list)
        for i in range(k-1):
            heappop(new_list)
        return -heappop(new_list)