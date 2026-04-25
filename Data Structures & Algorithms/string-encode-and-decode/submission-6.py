class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for tri in strs:
            num = len(tri)
            result += str(num) + "#"+ tri  
        return result 
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        num = 0
        while i < len(s):
            if (s[i] >= '0' and s[i] <= '9'):
                num = num * 10 + (ord(s[i]) - ord('0'))
                i = i + 1
            elif s[i] == "#":
                result.append(s[i + 1:i + num + 1])
                i = i + num + 1
                num = 0
        return result
