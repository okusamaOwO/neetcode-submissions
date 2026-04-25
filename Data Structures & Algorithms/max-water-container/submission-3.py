class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # too small i don't need you :|| 
        i = 0
        j = len(heights) - 1
        largest = 0 
        while (i < j):
            area = min(heights[i], heights[j]) * (j - i)
            if largest < area:
                largest = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return largest 

        