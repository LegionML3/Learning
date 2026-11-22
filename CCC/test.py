#Problem J3: Candy Box Counts

n = int(input())
table = input()
target = input()
l, r = map(int, input().split())

sliced = table[l - 1:r]

print(sliced.count(target))