# 1번 : deepcopy 사용, 조합 미사용. Python 시간초과, pypy만 통과
import sys, copy
from collections import deque
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

n, m = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))

answer = 0

def bfs():
    global answer
    arr = copy.deepcopy(graph)
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c]
                q.append((nr, nc))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

def dfs(x):
    if x == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(x + 1)
                graph[i][j] = 0

dfs(0)
print(answer)

#2번 : deepcopy, 조합 사용. Python도 통과가능한 코드
import sys, copy
from itertools import combinations
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

answer = 0
for comb in list(combinations(empty, 3)):
    arr = copy.deepcopy(graph)
    for r, c in comb:
        arr[r][c] = 1

    virus = [(i, j) for i in range(n) for j in range(m) if arr[i][j] == 2]
    while virus:
        r, c = virus.pop()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                arr[nr][nc] = 2
                virus.append((nr, nc))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

print(answer)