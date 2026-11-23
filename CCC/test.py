# J3 2A
# import sys

# n = sys.stdin.readline()
# old = sys.stdin.readline()
# new = sys.stdin.readline()

# count = 0
# for o, n in zip(old, new):
#     if o == 'C' and n == 'C':
#         count += 1

# print(count)

# J3 2B
# import sys

# n = sys.stdin.readline()
# game = sys.stdin.readline()

# streak = 0
# score = 0
# for char in game:
#     if char == 'W':
#         streak += 1
#         score += 1
#         if streak >= 3:
#             score += 2
#     else:
#         streak = 0

# print(score)