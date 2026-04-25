class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            num = len(s)
            result = result + str(num) + "#" + s
        return result 
    def decode(self, s: str) -> List[str]:
        result = []
        num = ""
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                num = num + s[i]
                i = i + 1
            elif s[i] == "#":
                element = ""
                len_str = int(num)
                for j in range(len_str):
                    element = element + s[i + j + 1]
                i = i + len_str + 1
                result.append(element)
                num = ""
        return result 
                