n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[r][c] = True
dr = (-1, 0, 1, 0) # 북, 동, 남, 서
dc = (0, 1, 0, -1)

def isPossible(x, y):
    return 0 <= x < n and 0 <= y < m

while True:
    check = False
    for _ in range(4):
        d = (d - 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if isPossible(nr, nc) and not arr[nr][nc] and not visited[nr][nc]:
            check = True
            visited[nr][nc] = True
            r, c = nr, nc
            break

    if not check:
        nr = r - dr[d]
        nc = c - dc[d]
        if isPossible(nr, nc):
            if arr[nr][nc]:
                break
            r, c= nr, nc
            
print(sum(sum(v) for v in visited))