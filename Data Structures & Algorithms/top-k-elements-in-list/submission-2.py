class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        sorted_dict = sorted(count.items(), key=lambda item: item[1], reverse = True)
        result = []
        for i, (key, value) in zip(range(k), sorted_dict):
            result.append(key)
        return result
