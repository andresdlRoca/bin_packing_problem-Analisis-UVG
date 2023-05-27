def bin_packing(items, bin_capacity):
    n = len(items)
    dp = [[0] * (bin_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, bin_capacity + 1):
            if items[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1] + dp[i - 1][j - items[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    bins = []
    i, j = n, bin_capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            bins.append(items[i - 1])
            j -= items[i - 1]
        i -= 1

    return bins

# Example usage
items = [2, 5, 4, 7, 1, 3, 8]
bin_capacity = 20
packed_items = bin_packing(items, bin_capacity)
print("Packed items:", packed_items)
print("Number of bins used:", len(packed_items))
