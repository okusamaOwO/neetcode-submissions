class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ngheo ngheo ngheo
        processed_s = ""
        for char in s:
            if '0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                processed_s += char.lower()
        # aba
        # aa
        # prepare 2 pointers 
        i = 0
        j = len(processed_s) - 1
        while(i < j):
            if processed_s[i] != processed_s[j]:
                return False
            i += 1
            j -= 1
        return True 
        