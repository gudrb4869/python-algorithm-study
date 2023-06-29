import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

low, high = 0, max(arr)
answer = 0

while low <= high:
    mid = (low + high) // 2
    total = 0
    for a in arr:
        if a > mid:
            total += a - mid
    if total < m:
        high = mid - 1
    else:
        low = mid + 1
        answer = mid

print(answer)