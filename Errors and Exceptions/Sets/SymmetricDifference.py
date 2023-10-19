M = int(input())
setM = set(list(map(int, input().split())))
N = int(input())
setN = set(list(map(int, input().split())))
s = (setN.union(setM)).difference((setM.intersection(setN)))
for x in sorted(list(s)):
    print(x)