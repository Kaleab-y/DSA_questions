n, m = [int(x.strip()) for x in input().split()]
a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]
for w in b:
    indices = [i+1 for i, x in enumerate(a) if x == w]
    if indices:
        print(*indices)
    else:
        print(-1)