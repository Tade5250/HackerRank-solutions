from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    key, value = input().rsplit(' ', 1)
    d[key] = d.get(key, 0) + int(value)

for key, value in d.items():
    print(key, value)