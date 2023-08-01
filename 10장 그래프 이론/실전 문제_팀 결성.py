import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def isUnion(a, b):
    return find(a) == find(b)

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    elif t == 1:
        if isUnion(a, b):
            print('YES')
        else:
            print('NO')