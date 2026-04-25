class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        for i in range (len(arr) - k + 1):
            s = 0
            for j in range(k):
                s  += arr[i + j]
            if s >= threshold * k:
                res += 1
        return res 