#J3 Art

xs = []
ys = []
for i in range(int(input())):
    x, y = input().split(',')
    xs.append(int(x))
    ys.append(int(y))


print(f'{min(xs) - 1}, {min(ys) - 1}')
print(f'{max(xs) + 1}, {max(ys) + 1}')
