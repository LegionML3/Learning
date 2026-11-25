#J3 Secret Cipher

input()
s = input()

i = 1
ans = []
for char in s:
    id = ord(char)
    if i % 2 == 0:
        if char == 'A':
            ans.append('Z')
        else:
            ans.append(chr(id - 1))

    else:
        if char == 'Z':
            ans.append('A')
        else:
            ans.append(chr(id + 1))

    i += 1

print(''.join(ans))