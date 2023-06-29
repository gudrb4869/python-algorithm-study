n = int(input())
dp = [0] * n
dp[0] = 1

two = three = five = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        two += 1
        next2 = dp[two] * 2
    if dp[i] == next3:
        three += 1
        next3 = dp[three] * 3
    if dp[i] == next5:
        five += 1
        next5 = dp[five] * 5

print(dp[-1])