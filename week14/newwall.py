def count(r):
    # Create a 2D array to store the minimum number of changes required for each cell
    dp = [[0 for _ in range(len(r[0]))] for _ in range(len(r))]
    # Set the value of the top left cell to 0
    dp[0][0] = 0
    # Iterate through the rows
    for i in range(1, len(r)):
        # Check if the current cell is a floor tile
        if r[i][0] == '.':
            # Set the value of the cell to the value of the cell above it
            dp[i][0] = dp[i-1][0]
        else:
            # Set the value of the cell to the value of the cell above it + 1
            dp[i][0] = dp[i-1][0] + 1
    # Iterate through the columns
    for j in range(1, len(r[0])):
        # Check if the current cell is a floor tile
        if r[0][j] == '.':
            # Set the value of the cell to the value of the cell to the left of it
            dp[0][j] = dp[0][j-1]
        else:
            # Set the value of the cell to the value of the cell to the left of it + 1
            dp[0][j] = dp[0][j-1] + 1
    # Iterate through the rows
    for i in range(1, len(r)):
        # Iterate through the columns
        for j in range(1, len(r[0])):
            # Check if the current cell is a floor tile
            if r[i][j] == '.':
                # Set the value of the cell to the minimum of the values of the cell above it and the cell to the left of it
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            else:
                # Set the value of the cell to the minimum of the values of the cell above it and the cell to the left of it + 1
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    # Return the value of the bottom right cell
    return dp[-1][-1]

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2