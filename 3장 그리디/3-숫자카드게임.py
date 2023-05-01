# n : 행, _ : 열
n, _ = map(int, input().split())
# 각 행의 카드 값 입력 후 최소값뽑아서 리스트 만들고 정렬뒤 최대값 출력
print(sorted(list(min(list(map(int, input().split()))) for i in range(n)))[-1])