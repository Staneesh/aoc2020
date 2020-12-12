operations = open("data", "r").read().split('\n')

# 0 - north, 1 - east, 2 - south, 3 - west
looking_dir = 1
x = y = 0

for op in operations:
    if len(op) < 2:
        continue

    what = op[0]
    arg = int(op[1:])

    if what == 'R':
        looking_dir = (looking_dir + arg/90)%4
    elif what == 'L':
        looking_dir = (looking_dir - arg/90)%4
    elif (what == 'F' and looking_dir == 0) or what == 'N':
        y += arg
    elif (what == 'F' and looking_dir == 1) or what == 'E':
        x += arg
    elif (what == 'F' and looking_dir == 2) or what == 'S':
        y -= arg
    elif (what == 'F' and looking_dir == 3) or what == 'W':
        x -= arg

print(f"x = {x}, y = {y}, dist = {abs(x)+abs(y)}")

    

