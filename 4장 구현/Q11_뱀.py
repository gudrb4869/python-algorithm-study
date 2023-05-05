from collections import deque
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

arr = [[0] * n for _ in range(n)] # 0: 빈칸, 1: 사과
for _ in range(k):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1 # 사과 위치 지정

dr = (0, 1, 0, -1) # 동 남 서 북
dc = (1, 0, -1, 0)

snake = deque([(0, 0)]) # 뱀이 있는 위치
d = 0
l = deque() # 뱀의 방향 변환 목록
for _ in range(int(input())):
    x, c = input().split()
    l.append((int(x), c))

time = 0
while True:
    time += 1
    r, c = snake[-1]
    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < n) or not (0 <= nc < n) or (nr, nc) in snake:
        break

    snake.append((nr, nc))
    if arr[nr][nc] == 0:
        snake.popleft()
    else:
        arr[nr][nc] = 0
    
    if l and time == l[0][0]:
        if l[0][1] == 'L':
            d = (d - 1) % 4
        elif l[0][1] == 'D':
            d = (d + 1) % 4
        l.popleft()

print(time)