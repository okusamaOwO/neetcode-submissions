class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] = count[ord(char) - ord('a')] + 1
            if tuple(count) in dic:
                dic[tuple(count)] = dic[tuple(count)] + [s]
            else:
                dic[tuple(count)] = [s]
        return list(dic.values())