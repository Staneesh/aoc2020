operations = open("data", "r").read().split('\n')

# 0 - north, 1 - east, 2 - south, 3 - west
looking_dir = 1
x = y = 0
wpx = 10
wpy = 1

for op in operations:
    if len(op) < 2:
        continue

    what = op[0]
    arg = int(op[1:])

    if what == 'F':
        x += wpx * arg
        y += wpy * arg

    elif what == 'N':
        wpy += arg
    elif what == 'E':
        wpx += arg
    elif what == 'S':
        wpy -= arg
    elif what == 'W':
        wpx -= arg
    
    elif what == 'R':
        for i in range(int(arg/90)):
            tmp = wpx
            wpx = wpy
            wpy  = -tmp
    elif what == 'L':
        for i in range(int(arg/90)):
            tmp = wpy
            wpy = wpx
            wpx  = -tmp
    
    print(f"OP: {what, arg} -> (x, y) = {x, y}, (wpx, wpy) = {wpx, wpy}")

print(f"x = {x}, y = {y}, dist = {abs(x)+abs(y)}")

    
