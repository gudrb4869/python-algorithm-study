n = input()
l = len(n)
print('LUCKY' if sum(map(int, list(n[:l//2]))) == sum(map(int, list(n[l//2:]))) else 'READY')