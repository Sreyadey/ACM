class prob2:
    def rec(self, arr, target, idx, ans, list):
        if idx == len(arr):
            if target == 0:
                ans.append(list[:])
            return
        if arr[idx] <= target:
            list.append(arr[idx])
            self.rec(arr, target - arr[idx], idx, ans, list)
            list.pop()
        self.rec(arr, target, idx + 1, ans, list)

    def combinationSum(self, candidates, target):
        ans = []
        list = []
        self.rec(candidates, target, 0, ans, list)
        return ans
