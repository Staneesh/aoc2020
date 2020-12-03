file = open("data", "r")

x     = [0] * 5
y     = [0] * 5
trees = [0] * 5
dx    = [1, 3, 5, 7, 1]
dy    = [1, 1, 1, 1, 2]

for (line, line_counter) in zip(file, range(400)):
    
    line_len = len(line) - 1
    if line_len < 30:
        break

    for (i, cdx, cdy, current_x, current_y) in zip(range(5), dx, dy, x, y):
        if line_counter % cdy == 0:
            if line[current_x] == '#':
                trees[i] = trees[i] + 1
            
            x[i] = (current_x + cdx)%line_len
            y[i] = (current_y + cdy)%line_len
            
        print(f"{line_counter}   [{cdx}, {cdy}]({current_x}, {current_y}): trees = {trees[i]}")

product = 1
for tree in trees:
    product = product * tree

print(f"trees: {product}")

file.close()