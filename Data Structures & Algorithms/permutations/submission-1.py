class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def tryy(current_elements):
            if not current_elements:
                result.append(path.copy())
                return
            for j in range(len(current_elements)):
                # what to do here?
                path.append(current_elements[j])
                remaining_elements = current_elements[:j] + current_elements[j+1:]
                tryy(remaining_elements)
                path.pop()
        tryy(nums)
        return result 