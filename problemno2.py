def combination_sum(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], target - candidates[i])

    res = []
    candidates.sort()
    backtrack(0, [], target)
    return res

