a = list(map(int, input().split()))
max1 = max(a)
a = [x for x in a if x != max1]
print(max(a))
