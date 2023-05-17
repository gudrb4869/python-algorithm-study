def solution(p):
    return dfs(p)

d = {'(':')', ')':'('}

def dfs(w):
    if w == '':
        return ''
    
    stack = []
    for i, c in enumerate(w):
        if stack and stack[-1] == d[c]:
            stack.pop()
            if not stack:
                u, v = w[:i + 1], w[i + 1:]
                break
        else:
            stack.append(c)
            
    stack = []
    for c in u:
        if c == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return '(' + dfs(v) + ')' + ''.join(d[i] for i in u[1:-1])
    return u + dfs(v)