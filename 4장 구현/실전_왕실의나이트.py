s = input()
r, c = int(s[1]), ord(s[0]) - ord('a') + 1
dr = (-2, -2, -1, -1, 1, 1, 2, 2)
dc = (-1, 1, -2, 2, -2, 2, -1, 1)
answer = 0
for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]

    if 1 <= nr <= 8 and 1 <= nc <= 8:
        answer += 1

print(answer)