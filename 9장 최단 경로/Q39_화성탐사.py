import heapq

INF = 1000000
direction = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 상 우 하 좌

def dijkstra():
    heap = [(0, 0, 0)]
    dist[0][0] = graph[0][0]

    while heap:
        weight, r, c = heapq.heappop(heap)

        if r == c == n - 1:
            return weight

        if weight > dist[r][c]:
            continue

        for dr, dc in direction:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n:
                W = dist[r][c] + graph[nr][nc]
                if dist[nr][nc] > W:
                    heapq.heappush(heap, (W, nr, nc))
                    dist[nr][nc] = W

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    print(dijkstra())