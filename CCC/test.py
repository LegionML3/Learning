#Cool Zip Problem

n = int(input())
a = []
c = 0
for i in range(n*2):
    raw = input()
    a.append(raw)

stu, key = a[:n], a[n:]

for s, k in zip(stu, key):
    if s == k:
        c += 1

print(c)