#J4 The Circular Train Route

stations = int(input().split()[0])
forwards = [int(f) for f in input().split()]
visited = set()
print(stations)
print(forwards)

current = 0
for des in range(len(forwards)):
    current += forwards[des]

print(current)
print(current % stations - 1)
