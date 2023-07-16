import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]

    while q:
        weight, now = heapq.heappop(q)

        if weight > dist[now]:
            continue

        for nxt, cost in graph[now]:
            W = weight + cost
            if dist[nxt] > W:
                dist[nxt] = W
                heapq.heappush(q, (dist[nxt], nxt))

dijkstra(c)

cnt, time = 0, 0
for i in range(1, n + 1):
    if i != c and dist[i] != INF:
        cnt += 1
        time = max(time, dist[i])
print(cnt, time)