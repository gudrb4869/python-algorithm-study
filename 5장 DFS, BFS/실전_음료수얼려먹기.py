# BFS
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
answer = 0
directions = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상, 우, 하, 좌

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))
            answer += 1
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

print(answer)

# DFS
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상, 우, 하, 좌

def dfs(r, c):
    visited[r][c] = True
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and not visited[nr][nc]:
            dfs(nr, nc)

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            answer += 1

print(answer)