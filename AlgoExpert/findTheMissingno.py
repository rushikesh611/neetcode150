def getMissingNo(arr):
    n = len(arr)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A