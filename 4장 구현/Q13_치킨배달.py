from itertools import combinations
INF = int(1e9)

n, m = map(int, input().split())
home = []
chicken = []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            home.append((i, j))
        elif l[j] == 2:
            chicken.append((i, j))

answer = INF # 도시의 치킨 거리의 최솟값
for comb in list(combinations(chicken, m)):
    candidate = 0 # 도시의 치킨 거리(후보)
    for h in home:
        dist = INF # 집의 치킨 거리
        for c in comb:
            dist = min(dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        candidate += dist
    answer = min(answer, candidate)
print(answer)