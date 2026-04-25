class Solution:
    def binarySearch(self, numbers: List[int], target: int) -> int:
        low = 0
        high = len(numbers) - 1
        middle = 0
        while(low <= high):
            middle = int((high + low) / 2)
            if numbers[middle] == target:
                return middle 
            if numbers[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return -1 

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(numbers):
            phan_bu = target - num
            if self.binarySearch(numbers[i+1:], phan_bu) == -1:
                continue
            else:
                return [i + 1, self.binarySearch(numbers[i+1:], phan_bu) + i + 2]
        return 0