# Problem J3: The Bounding Box Explorer

# An archaeological explorer is mapping out an ancient grid-based site.
# The explorer starts at the origin coordinate $(0, 0)$.

# They follow a sequence of $N$ movement instructions. Each instruction consists of a direction 
# character (U for Up, D for Down, L for Left, R for Right) and an integer distance $D$.
#  - U increases the $y$-coordinate by $D$ ($y \leftarrow y + D$)
#  - D decreases the $y$-coordinate by $D$ ($y \leftarrow y - D$)
#  - L decreases the $x$-coordinate by $D$ ($x \leftarrow x - D$)
#  - R increases the $x$-coordinate by $D$ ($x \leftarrow x + D$)

# As the explorer moves from point to point, we want to find the bounding box that encloses
# every single position they ever occupy (including the starting position $(0, 0)$
# and the endpoint of every move).

# Your task is to find four values:
#  The minimum $x$-coordinate reached (min_x)
#  The maximum $x$-coordinate reached (max_x)
#  The minimum $y$-coordinate reached (min_y)
#  The maximum $y$-coordinate reached (max_y)

#Input Specification
#  The first line contains an integer $N$ ($1 \le N \le 1000$), the number of movement instructions.
#  The next $N$ lines each contain a character (U, D, L, or R) followed by a space and an integer $D$ ($1 \le D \le 100$), 
#  representing the distance moved in that direction.

#Output Specification
#  Output four space-separated integers on a single line: min_x, max_x, min_y, and max_y.

n = int(input())
min_y = 0
min_x = 0
max_y = 0
max_x = 0
current_pos = [0, 0]
for i in range(n):
    direction, raw_s = input().split()
    step = int(raw_s)
    if direction == 'R':
        current_pos[0] += step
    elif direction == 'L':
        current_pos[0] -= step
    elif direction == 'U':
        current_pos[1] += step
    elif direction == 'D':
        current_pos[1] -= step
    
    if current_pos[0] > max_x:
        max_x = current_pos[0]
    if current_pos[0] < min_x:
        min_x = current_pos[0]

    if current_pos[1] > max_y:
        max_y = current_pos[1]
    if current_pos[1] < min_y:
        min_y = current_pos[1]

print(min_x, max_x, min_y, max_y)