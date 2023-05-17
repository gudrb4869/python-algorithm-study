from itertools import combinations
import copy

n = int(input())
arr = [list(input().split()) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 'X']

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def move(arr, r, c, k):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    if arr[r][c] == 'O':
        return True
    if arr[r][c] == 'S':
        return False
    return move(arr, r + dr[k], c + dc[k], k)

def solve():
    for comb in list(combinations(empty, 3)):
        copy_arr = copy.deepcopy(arr)
        for r, c in comb:
            copy_arr[r][c] = 'O'

        teacher = [(i, j) for i in range(n) for j in range(n) if copy_arr[i][j] == 'T']
        check = True
        for r, c in teacher:
            for k in range(4):
                check &= move(copy_arr, r, c, k)
                if not check:
                    break
        if check:
            return True
    
    return False

print('YES' if solve() else 'NO')