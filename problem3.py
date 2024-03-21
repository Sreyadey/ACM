def can_make_zero(arr):
    n = len(arr)
    for i in range(n - 1):
        arr[i + 1] -= arr[i]
        arr[i] = 0
        if arr[i + 1] < 0:
            return "NO"
    if arr[-1] != 0:
        return "NO"
    return "YES"
