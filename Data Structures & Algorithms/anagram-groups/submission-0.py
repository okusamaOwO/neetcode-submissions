class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorted_ver = "".join(sorted(s))
            if not sorted_ver in dic:
                 dic[sorted_ver] = [s]
            else:
                dic[sorted_ver] = dic[sorted_ver] + [s]
        result = []
        for key in dic:
            result = result + [dic[key]]
        return result 