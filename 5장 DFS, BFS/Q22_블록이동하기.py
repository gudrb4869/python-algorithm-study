# 옛날에 푼거
from collections import deque

def solution(board):
    n = len(board)
    arr = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            arr[i + 1][j + 1] = board[i][j]
            
    dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
    q = deque([(1, 1, 1, 2, 0)])
    visited = set([(1, 1, 1, 2)])
    while q:
        r1, c1, r2, c2, t = q.popleft()
        if r1 == c1 == n or r2 == c2 == n:
            return t
        
        cand = []
        for i in range(4):
            nr1, nc1 = r1 + dr[i], c1 + dc[i]
            nr2, nc2 = r2 + dr[i], c2 + dc[i]
            if arr[nr1][nc1] == 0 and arr[nr2][nc2] == 0:
                cand.append((nr1, nc1, nr2, nc2))
            
        if r1 == r2:
            for d in (-1, 1):
                if arr[r1 + d][c1] == 0 and arr[r2 + d][c2] == 0:
                    cand.append((r1, c1, r1 + d, c1))
                    cand.append((r2, c2, r2 + d, c2))
        else:
            for d in (-1, 1):
                if arr[r1][c1 + d] == 0 and arr[r2][c2 + d] == 0:
                    cand.append((r1, c1, r1, c1 + d))
                    cand.append((r2, c2, r2, c2 + d))
        
        for nxt in cand:
            if nxt not in visited:
                visited.add(nxt)
                q.append((*nxt, t + 1))

#################
# 5월 8일에 푼거
from collections import deque

dr = (0, 1, 0, -1) # 동 남 서 북
dc = (1, 0, -1, 0) # 동 남 서 북

def solution(board):
    n = len(board)
    arr = [[1] * (n + 2) for _ in range(n + 2)]
    visited = [[[False] * 4 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            arr[i + 1][j + 1] = board[i][j]
            
    q = deque([(1, 1, 0, 0)]) # 기준축 행, 기준축 열, 기준축 기준으로 다른축이 있는 방향, 현재 소비 시간
    visited[1][1][0] = visited[1][2][2] = True
    while q:
        r1, c1, d, t = q.popleft()
        r2, c2 = r1 + dr[d], c1 + dc[d]
        
        if (n, n) in ((r1, c1), (r2, c2)):
            return t
        
        for k in range(4):
            nr1, nc1 = r1 + dr[k], c1 + dc[k]
            nr2, nc2 = r2 + dr[k], c2 + dc[k]
            
            if arr[nr1][nc1] == arr[nr2][nc2] == 0:
                if k in ((d - 1) % 4, (d + 1) % 4):
                    if not visited[r1][c1][k] and not visited[nr1][nc1][(k + 2) % 4]:
                        visited[r1][c1][k] = visited[nr1][nc1][(k + 2) % 4] = True
                        q.append((r1, c1, k, t + 1))
                    if not visited[r2][c2][k] and not visited[nr2][nc2][(k + 2) % 4]:
                        visited[r2][c2][k] = visited[nr2][nc2][(k + 2) % 4] = True
                        q.append((r2, c2, k, t + 1))
                if not visited[nr1][nc1][d] and not visited[nr2][nc2][(d + 2) % 4]:
                    visited[nr1][nc1][d] = visited[nr2][nc2][(d + 2) % 4] = True
                    q.append((nr1, nc1, d, t + 1))