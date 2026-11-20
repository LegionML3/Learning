#J4 The Circular Train Route

stations = int(input().split()[0])
forwards = [int(f) for f in input().split()]
visited = set()

cur = 1
visited.add(cur)
for step in forwards:
    
    cur += step
    while cur > stations:
        cur -= stations

    if not cur in visited:
        visited.add(cur)

print(cur)
print(len(visited))
