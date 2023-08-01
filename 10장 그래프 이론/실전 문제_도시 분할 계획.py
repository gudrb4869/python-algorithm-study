import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m =map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
max_cost = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        max_cost = max(max_cost, cost)
        result += cost

print(result - max_cost)