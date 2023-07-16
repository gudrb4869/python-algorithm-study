import sys
input = sys.stdin.readline
INF = int(1e9) # 무한대값 설정
n, m = map(int, input().split()) # 학생수, 성적비교횟수

graph = [[INF] * n for _ in range(n)] # 2차원배열 무한대값으로 세팅
for i in range(n):
    graph[i][i] = 0 # 자기자신에게 가는 경로는 0으로 세팅

for _ in range(m):
    a, b = map(int ,input().split())
    graph[a - 1][b - 1] = 1 #  A에서 B로 가는 경로 1로 세팅

# 플로이드 워셜 알고리즘 수행
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(n):
    count = 0 # i번 학생 기준으로 성적을 알수 있는 학생의 수
    for j in range(n):
        # j번 학생에서 오는 경로와 j번 학생으로 가는 경로 둘중 하나라도 무한대값이 아니면 성적파악가능하므로 count값 1증가
        # 이때 i번 학생 자기자신에서 오는 경로나 자기자신으로 가는 경로는 0이므로 이때도 count됨
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    # count값이 학생수와 같으면 i번 학생의 성적 순위 정확히 알 수있으므로 answer 1증가
    if count == n:
        answer += 1

print(answer) # 결과값 출력