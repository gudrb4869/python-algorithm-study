# 문자열 s의 각 문자들을 int 타입으로 치환 후 리스트로 변환함.
s = list(map(int, list(input())))
result = 0
for i in s:
    # 결과값이 0, 1이거나, s의 i번째 인덱스의 값이 0, 1인경우 더함.
    if i <= 1 or result <= 1:
        result += i
    else: # 결과값, s의 i번째 인덱스의 값이 0, 1이 아니면 곱함.
        result *= i
print(result)