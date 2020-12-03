file = open("data", "r")

x     = [0, 0, 0, 0, 0]
y     = [0, 0, 0, 0, 0]
dx    = [1, 3, 5, 7, 1]
dy    = [1, 1, 1, 1, 2]
trees = [0, 0, 0, 0, 0]
product = 1

n = len(dx)
line_counter = 0

for line in file:
    line_len = len(line) - 1
    if line_len < 30:
        break

    for i in range(n):
        cdx = dx[i]
        cdy = dy[i]
        current_x = x[i]
        current_y = y[i]

        if line_counter % cdy == 0:
            if line[current_x] == '#':
                trees[i] = trees[i] + 1
            
            x[i] = (current_x + cdx)%line_len
            y[i] = (current_y + cdy)%line_len
            
        print(f"{line_counter}   [{cdx}, {cdy}]({current_x}, {current_y}): trees = {trees[i]}")



    line_counter = line_counter + 1

for tree in trees:
    product = product * tree

print(f"trees: {product}")

file.close()