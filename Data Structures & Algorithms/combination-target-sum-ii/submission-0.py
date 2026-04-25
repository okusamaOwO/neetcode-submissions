class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        def tryy(path, start_index):
            if sum(path) > target:
                return
            if sum(path) == target:
                result.append(path.copy())
                return
            # chỗ này là phải làm như nào
            s = set()
            for j in range(start_index, len(candidates)):
                if candidates[j] in s:
                    continue
                else:
                    s.add(candidates[j])
                path.append(candidates[j])
                tryy(path, j + 1)
                path.pop()
        tryy(path, 0)
        return [x for x in result]