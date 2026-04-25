class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use map instead 
        dic = {}
        
        for i, num in enumerate(nums):
            phan_bu = target - num
            if not phan_bu in dic:
                dic[num] = i
            else:
                result = [dic[phan_bu], i]
                return result



            