#J3 Ball Swap / Cup Shuffle

a = ['ball', 'empty', 'empty']
n = int(input())
for i in range(n):
    ori, swap = map(int, input().split())
    ori -= 1
    swap -= 1

    change = a[ori]

    a[ori] = a[swap]
    a[swap] = change
    


print(a.index('ball') + 1)