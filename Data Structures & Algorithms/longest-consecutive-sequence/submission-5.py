class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        longest = 0
        for num in s:
            previous = num - 1
            if previous not in s: # it will be the beginning of a streak 
                streak = 1
                while (num + streak) in s:
                    streak += 1
                longest = max(streak, longest)
                    
        return longest 