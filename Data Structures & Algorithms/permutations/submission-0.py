class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
         # check whether nums is empty
        
        def tryy(current_nums):
            if not current_nums: # if no numbers left
                result.append(path.copy())
                return 
            for j in range(len(current_nums)):
                num = current_nums[j]
                path.append(num)
                remaining_nums = current_nums[:j] + current_nums[j+1:]
                tryy(remaining_nums)
                path.pop()
        tryy(nums)
        return result