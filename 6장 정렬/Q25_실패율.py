def solution(N, stages):
    dp = [0] * (N + 1) # 스테이지 도달인원 구하기 위해 누적합 사용
    d = dict((i + 1, 0) for i in range(N)) # 각 스테이지 도달 인원 수 0으로 세팅
    
    for s in stages:
        dp[1] += 1 # 1단계 1증가
        if s < N + 1:
            dp[s] -= 1 # s단계가 N + 1 미만일 때 s단계 1감소
    
    cur = len(stages) # stages 리스트의 길이 = 초기 사용자 수
    
    for i in range(1, N + 1):
        dp[i] += dp[i - 1] # i단계 일때 i - 1단계의 도달 인원 수 더해서 i단계 도달인원계산
        if cur > 0: # 현재 남은 인원이 0이상일때만 실패율 계산. 0으로 나누는거 방지
            d[i] = (cur - dp[i]) / cur # (현재 남은 인원 - 현재스테이지 도달인원) / 현재 남은 인원
            cur = dp[i] # 현재 남은 인원을 i번째 스테이지의 도달인원수로 할당
    
    # 딕셔너리 d를 key, value 쌍으로 갖는 리스트로 만들고 value를 기준으로 내림차순 정렬함
    # 그리고 정렬된 리스트에서 key 값만 리스트로 따로 추출하여 리턴
    return list(l[0] for l in sorted(list(d.items()), key=lambda x: -x[1]))