from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque([(0, 0, 1)]) # 행, 열, 현재 이동 칸의 개수
visited[0][0] = True
delta = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상, 우, 하, 좌
while q:
    r, c, t = q.popleft()
    if (r, c) == (n - 1, m - 1):
        print(t)
        break

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc, t + 1))