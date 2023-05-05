d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

n = int(input())
r, c = 1, 1
for v in list(input().split()):
    if 1 <= r + d[v][0] <= n and 1 <= c + d[v][1] <= n:
        r += d[v][0]
        c += d[v][1]

print(r, c)