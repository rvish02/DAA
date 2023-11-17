def solve_knapsack():
    val = [50, 100, 150, 200]
    wt = [8, 16, 32, 40]
    W = 64
    n = len(val) - 1  # Index of the last item

    # Memoization table to store results of subproblems
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def knapsack(W, n):
        if n < 0 or W < 0:
            return 0

        # Check if the result is already calculated
        if memo[n][W] != -1:
            return memo[n][W]

        if wt[n] > W:
            result = knapsack(W, n - 1)
        else:
            include_current = val[n] + knapsack(W - wt[n], n - 1)
            exclude_current = knapsack(W, n - 1)
            result = max(include_current, exclude_current)

        # Save the result in the memoization table
        memo[n][W] = result

        return result

    print(knapsack(W, n))

if __name__ == "__main__":
    solve_knapsack()
