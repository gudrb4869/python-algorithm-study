# 1
def solution(s):
    l = len(s)
    answer = l
    for i in range(1, l // 2 + 1):
        cnt = 0
        result = []
        for j in range(0, l, i):
            cur = s[j : j + i]
            if result and result[-1][0] == cur:
                result[-1][1] += 1
            else:
                result.append([cur, 1])
        
        length = 0
        for r in result:
            if r[1] > 1:
                length += len(str(r[1]))
            length += len(r[0])
        answer = min(answer, length)
    return answer

# 2
def solution(s):
    l = len(s)
    answer = l
    for i in range(1, l // 2 + 1):
        cnt = 0
        prev = s[:i]
        result = ''
        for j in range(0, l, i):
            cur = s[j : j + i]
            if prev == cur:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt)
                result += prev
                cnt = 1
                prev = cur
        if cnt > 1:
            result += str(cnt)
        result += prev
        answer = min(answer, len(result))
    return answer