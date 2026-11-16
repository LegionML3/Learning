#sliding window
n = int(input())
ans = []
for i in range(n):
    string = input()
    items = []
    counts = []
    count = 0
    if len(string) == 1:
        counts.append(1)
        items.append(string[0])
    for j in range(len(string) - 1):

        if string[j] == string[j + 1]:
            count += 1
        else:
            items.append(string[j])
            count += 1
            counts.append(count)
            count = 0

        if j + 1 == len(string) - 1:
            items.append(string[j + 1])
            count += 1
            counts.append(count)
    ans.append([str(count)+item for count, item in zip(counts, items)])

for batch in ans:
    print(" ".join(batch))