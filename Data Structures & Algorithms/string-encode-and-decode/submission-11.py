class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            num = len(s)
            result = result + str(num) + "#" + s
        return result 
    def decode(self, s: str) -> List[str]:
        result = []
        num = 0
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                num = num * 10 + ord(s[i]) - ord('0')
                i = i + 1
            elif s[i] == "#":
                result.append(s[i + 1 : i + 1 + num])
                i = i + num + 1
                num = 0
        return result 
                