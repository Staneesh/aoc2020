import time

def seat_good(x, y, seat, rows_prev, leny, lenx):
    occupied = [0] * 8
    empty = [0] * 8
    #checking horizontally right
    for i in range(x+1, lenx):
        seat = list(rows_prev[y])[i]
        if seat == 'L':
            empty[0] += 1
            break
        elif seat == '#':
            occupied[0] += 1
            break
    #checking horizontally left
    for i in range(x-1, -1, -1):
        seat = list(rows_prev[y])[i]
        if seat == 'L':
            empty[1] += 1
            break
        elif seat == '#':
            occupied[1] += 1
            break
    #checking vertically up
    for i in range(y + 1, leny):
        seat = list(rows_prev[i])[x]
        if seat == 'L':
            empty[2] += 1
            break
        elif seat == '#':
            occupied[2] += 1
            break
    #checking vertically down
    for i in range(y -1, -1 , -1):
        seat = list(rows_prev[i])[x]
        if seat == 'L':
            empty[3] += 1
            break
        elif seat == '#':
            occupied[3] += 1
            break
    #checking diagonal right up
    for (i, j) in zip(range(x + 1, lenx , 1), range(y+1, leny, 1)):
        if i < 0 or i >= lenx or j < 0 or j >= leny:
            break
        seat = list(rows_prev[j])[i]
        if seat == 'L':
            empty[4] += 1
            break
        elif seat == '#':
            occupied[4] += 1
            break
    #checking diagonal right down
    for (i, j) in zip(range(x + 1, lenx , 1), range(y-1, -1, -1)):
        if i < 0 or i >= lenx or j < 0 or j >= leny:
            break
        seat = list(rows_prev[j])[i]
        if seat == 'L':
            empty[5] += 1
            break
        elif seat == '#':
            occupied[5] += 1
            break    
    #checking diagonal left up
    for (i, j) in zip(range(x - 1, -1 , -1), range(y+1, leny, 1)):
        if i < 0 or i >= lenx or j < 0 or j >= leny:
            break
        seat = list(rows_prev[j])[i]
        if seat == 'L':
            empty[6] += 1
            break
        elif seat == '#':
            occupied[6] += 1
            break
    #checking diagonal left down
    for (i, j) in zip(range(x - 1, -1, -1), range(y-1, -1, -1)):
        if i < 0 or i >= lenx or j < 0 or j >= leny:
            break
        seat = list(rows_prev[j])[i]
        if seat == 'L':
            empty[7] += 1
            break
        elif seat == '#':
            occupied[7] += 1
            break    

    return (empty, occupied)
        
rows = open("data", "r").read().split('\n')

rows_prev = rows.copy()
rows_now = rows.copy()

while True:
    for (y, row_p) in zip(range(100), rows_prev):
        if len(row_p) < 5:
            continue
        
        for (x, seat) in zip(range(100), row_p):
            (empty_l, occupied_l) = seat_good(x, y, seat, rows_prev, len(rows), len(rows[0]))
            empty = occupied = 0
            for e in empty_l:
                empty += e
            for o in occupied_l:
                occupied += o

            #print(f"{y}, {x} ({seat}) : e = {empty_l},  o = {occupied_l}")
            if seat == 'L' and occupied == 0:
                s = list(rows_now[y])
                s[x] = '#'
                rows_now[y] = "".join(s)
            elif seat == '#' and occupied >= 5:
                s = list(rows_now[y])
                s[x] = 'L'
                rows_now[y] = "".join(s)
            else:
                s = list(rows_now[y])
                g = list(rows_prev[y])
                s[x] = g[x]
                rows_now[y] = "".join(s)

    #print("\n".join(rows_prev))
    
    #time.sleep(1)
    if rows_now == rows_prev:
        break

    tmp = rows_now.copy()
    rows_now = rows_prev.copy()
    rows_prev = tmp.copy()

table = "\n".join(rows_prev)
#print(table)

final = 0
for c in table:
    if c == '#':
        final += 1

print(final)