import sys
input = sys.stdin.readline
n = int(input()) # 원소의 개수
arr = list(map(int, input().split())) # n개의 원소 입력

def binary_search():
    left, right = 0, n - 1 # 시작점, 끝점
    while left <= right: # 반복 조건
        mid = (left + right) // 2 # 중간점
        if arr[mid] == mid: # 고정점. 원소 값이 인덱스와 동일함
            return mid
        elif arr[mid] < mid: # 원소값이 인덱스보다 작은 경우 시작점 변경
            left = mid + 1
        else: # 원소값이 인덱스보다 큰 경우 끝점 변경
            right = mid - 1
    return -1 # 고정점이 없는 경우

# 출력
print(binary_search())