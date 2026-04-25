class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        initial = []
        n = len(nums)
        def tryy(i):
            if i == n:
                result.append(initial.copy())
                print(f"with i {i} initial like this {initial}")
                return
            for j in range(2):
                # accept to append i
                if j == 0:
                    initial.append(nums[i])
                    print(f"with i {i} and j {j} the initial will be {initial}")
                    tryy(i+1)
                else:
                    initial.pop()
                    tryy(i+1)

                
        tryy(0)
        return result 