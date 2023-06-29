import sys
input = sys.stdin.readline
n, m = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort()
INF = 100000000
d = [INF] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(coin[i], m + 1):
        if d[j - coin[i]] != INF:
            d[j] = min(d[j - coin[i]] + 1, d[j])

if d[m] == INF:
    print(-1)
else:
    print(d[m])