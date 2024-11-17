A = set(input().split())
n = int(input())
R = True
for _ in range(n):
    B = set(input().split())
    if not A >= B:
        R = False
        break
print(R)