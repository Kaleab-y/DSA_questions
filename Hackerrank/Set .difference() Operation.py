en = int(input())
e = list(map(int, input().split()))[:en]
fr = int(input())
f = list(map(int, input().split()))[:fr]
print(len(list(set(e).difference(f))))