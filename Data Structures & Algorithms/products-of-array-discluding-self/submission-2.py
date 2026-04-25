class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = 0
        multiple = 1
        for num in nums:
            if num == 0:
                count0 += 1
            else:
                multiple = multiple * num
        
        result = [0] * len(nums)
        if count0 == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    result[i] = multiple
            return result

        elif count0 > 1:
            return [0] * len(nums)

        else:
            for i, num in enumerate(nums):
                result[i] = int(multiple / num)
            return result
        