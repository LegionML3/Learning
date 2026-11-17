#CCC '21 J3 - Secret Instructions

ans = []
while True:
    raw = input()
    if raw == '99999':
        break

    s = int(raw[0]) + int(raw[1])
    if not s:
        if 'left' in ans[-1]:
            ans.append(f'left {raw[2:]}')
        elif 'right' in ans[-1]:
            ans.append(f'right {raw[2:]}')
    elif s % 2 == 0:
        ans.append(f'right {raw[2:]}')
    else:
        ans.append(f'left {raw[2:]}')

for res in ans:
    print(res)