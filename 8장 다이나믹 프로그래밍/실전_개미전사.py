n = int(input())
l = list(map(int, input().split()))
d = [0] * n
d[0] = l[0]
d[1] = max(l[0], l[1])

for i in range(2, n):
    d[i] = max(d[i - 2] + l[i], d[i - 1])

print(d[-1])