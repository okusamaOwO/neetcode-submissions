class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0 
        r = k - 1
        res = 0 
        first_sum = 0

        for i in range(l, r+1):
            first_sum += arr[i]

        if first_sum >= threshold * k:
            res += 1

        while r < len(arr) - 1:
            r += 1
            first_sum += arr[r]
            first_sum -= arr[l]
            l += 1
            if first_sum >= threshold * k:
                res += 1
        return res 

