#J3 Ball Swap / Cup Shuffle

n = int(input())
ball_pos = 1
for i in range(n):
    ori, swap = map(int, input().split())
    if ball_pos == ori:
        ball_pos = swap
    elif ball_pos == swap:
        ball_pos = ori
    
print(ball_pos)