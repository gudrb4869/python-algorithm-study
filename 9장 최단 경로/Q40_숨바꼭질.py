import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dist = [INF] * (n + 1)
dist[1] = 0
q = [(0, 1)]

while q:
    weight, i = heapq.heappop(q)

    if weight > dist[i]:
        continue

    for j, _ in enumerate(graph[i]):
        W = dist[i] + graph[i][j]
        if W < dist[j]:
            dist[j] = W
            heapq.heappush(q, (W, j))

ans = max(dist[1:])
print(dist.index(ans), ans, dist.count(ans))