import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
cnt = 0
# 모험가의 공포도를 오름차순으로 정렬후,
# 각 그룹의 인원수(cnt) 1더하고 그룹수(cnt)가 해당 모험가의 공포도(a)보다 크거나 같으면
# 답(ans) 1증가시키고 cnt 0으로 초기화
for a in arr:
    cnt += 1
    if cnt >= a:
        ans += 1
        cnt = 0
    
print(ans)