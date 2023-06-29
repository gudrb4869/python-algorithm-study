import sys
input = sys.stdin.readline

def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return 'yes'
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 'no'

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
request = list(map(int, input().split()))
print(*[binary_search(arr, 0, n - 1, r) for r in request])