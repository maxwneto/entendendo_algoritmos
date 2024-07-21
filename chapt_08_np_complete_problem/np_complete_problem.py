def knapsack(capacity, weights, values, n):
    """
    Solve the knapsack problem by dynamic programming.
    
    Args:
    capacity (int): Maximum weight the knapsack can carry.
    weights (list of int): List of weights of the items.
    values (list of int): List of values of the items.
    n (int): Number of items.
    
    Returns:
    int: The maximum value that can be put in a knapsack of the given capacity.
    """
    # Create a 2D array to store the maximum value that can be obtained
    # for each sub-problem.
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
    # Build table dp[][] in a bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]


# Example usage:
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
n = len(weights)

max_value = knapsack(capacity, weights, values, n)
print(f"The maximum value that can be put in a knapsack of capacity {capacity} is {max_value}")
