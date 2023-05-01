import sys

input = sys.stdin.readline

# n : 배열의 크기
# m : 숫자가 더해지는 횟수
# k : 배열의 특정 인덱스 값을 연속해서 더할 수 있는 최대 횟수(인덱스 다르면 다른 숫자로 간주)
n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 1, 2번째로 가장 큰 동전
first, second = nums[-1], nums[-2]

# cnt: 첫번째 동전의 횟수
cnt = (m // (k + 1)) * k + (m % (k + 1))
ans = cnt * first + (m - cnt) * second
print(ans)