#J4 Frequent Flavors / Top Bucket

input()
orders = list(map(int, input().split()))

freq = [0] * 1001

for o in orders:
    freq[o] += 1

print(max(freq))