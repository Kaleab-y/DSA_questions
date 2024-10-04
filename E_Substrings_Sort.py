def is_Substring(a, b):
    return a in b
n = int(input())
strg = [input().strip() for _ in range(n)]
strg.sort(key=len)
valid = True
for i in range(1, n):
    if not is_Substring(strg[i-1], strg[i]):
        valid = False
if valid:
    print("YES")
    for s in strg:
        print(s)
else:
    print("NO")
