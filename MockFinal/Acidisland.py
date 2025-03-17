def largest_square_land(N, M, grid):
    # ผมใช้ chat gen คับ
    dp = [[0] * M for _ in range(N)]
    max_side = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                max_side = max(max_side, dp[i][j])
    print(dp)
    return max_side * max_side


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(largest_square_land(N, M, grid))
# ผมใช้ chat gen คับ