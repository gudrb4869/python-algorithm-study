import sys
input = sys.stdin.readline

n = int(input())

a = []
for _ in range(n):
    name, score = input().split()
    a.append((name, int(score)))

print(*[n for n, _ in sorted(a, key=lambda x: x[1])])