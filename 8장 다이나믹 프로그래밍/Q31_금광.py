t = int(input()) # 테스트 케이스

for _ in range(t):
    n, m = map(int, input().split()) # n * m 크기의 금광
    temp = list(map(int, input().split())) # n * m개의 위치에 매장된 금의 개수

    array = [[0] * m for _ in range(n)] # n * m 크기의 2차원 배열
    for i in range(n):
        for j in range(m):
            array[i][j] = temp[i * m + j] # 1차원 배열로 받았던 입력을 2차원 배열로 변환시켜줌
            
    array = []
    for i in range(n):
        array.append(temp[i * m : (i + 1) * m])

    dp = [[0] * m for _ in range(n)] # dp 테이블
    for i in range(n):
        dp[i][0] = array[i][0] # dp 테이블의 0번째 열값들을 금광의 0번째 열값으로 초기화

    for j in range(1, m): # 1번째 열부터 시작
        for i in range(n): # 행
            for d in (-1, 0, 1): # 왼쪽 위, 왼쪽, 왼쪽 아래
                if -1 < i - d < n: # (i, j)위치 기준으로 i - d의 행값이 금광 범위 내에 있는지 체크
                    dp[i][j] = max(dp[i][j], dp[i - d][j - 1] + array[i][j]) # 최대값으로 변경

    print(max(dp[i][-1] for i in range(n))) # dp 테이블의 마지막 열값중 최대값 출력