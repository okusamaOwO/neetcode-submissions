class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # chả lẽ lại dùng một cái map ? 
        m = {}
        # from heapq import heapify, heappop, heappush
        distances = []
        # heapify(distances)
        for point in points:
            x, y = point[0], point[1]
            distance = x*x + y*y
            distances.append(distance)
            if distance in m:
                m[distance] = m[distance] + [point]
            else:
                m[distance] = [point]
        distances.sort()
        result = []
        i = 0
        while len(result) < k:
            result = result + m[distances[i]]
            i += 1 
        return result 
    