class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # okay go go 
        from heapq import heapify, heappop, heappush
        heap = []
        heapify(heap)
        
        for point in points:
            x, y = point[0], point[1]
            distance = x * x + y * y
            heappush(heap, [-distance, point])
            while len(heap) > k:
                heappop(heap)
        return [x[1] for x in heap]
            
    