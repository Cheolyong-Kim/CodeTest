n = int(input())
find_number = int(input())
board = [[0] * n for _ in range(n)]

x, y = 0, 0
direction = 0
# 아래, 오른, 위, 왼
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for i in range(n * n, 0, -1):
    if i == find_number:
        find_x, find_y = x + 1, y + 1

    board[x][y] = i
    dx, dy = dxy[direction]
    nx, ny = x + dx, y + dy

    # 1. 정상 범위
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
    # 2. 인덱스를 벗어나거나, 다른 숫자 있음
    else:
        direction = (direction + 1) % 4
        dx, dy = dxy[direction]
        nx, ny = x + dx, y + dy
        x, y = nx, ny
