class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        longest = 1
        previous = nums[0]
        leng = 1
        for num in nums[1:]:
            if num == previous + 1:
                leng = leng + 1
                previous = num
                if longest < leng:
                    longest = leng
            elif num == previous:
                leng = leng
            else:
                leng = 1
                previous = num
        return longest 