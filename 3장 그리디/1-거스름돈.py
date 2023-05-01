n = int(input())
ans = 0

coins = [500, 100, 50, 10]

for coin in coins:
    ans += n // coin
    n %= coin

print(ans)