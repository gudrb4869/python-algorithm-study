import sys
input = sys.stdin.readline
n = int(input())

s = []
for _ in range(n):
    n, k, e, m = input().split() # 이름, 국어, 영어, 수학
    k, e, m = int(k), int(e), int(m)
    s.append((n, k, e, m))

s.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for n, _, _, _ in s:
    print(n)