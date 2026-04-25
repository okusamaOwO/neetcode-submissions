class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort hai cái array lại xong r so sánh ? 
        return sorted(s) == sorted(t)