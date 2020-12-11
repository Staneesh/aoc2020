import time

def seat_good(x, y, seat, rows_prev, leny, lenx):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, 0, -1, 1, 0,  -1, 1, -1]
    in_range = []
    vacant = 0
    n_seats = 0

    for (cdx, cdy) in zip(dx, dy):
        xnow = x + cdx
        ynow = y + cdy
        
        if xnow >= 0 and xnow < lenx and ynow >= 0 and ynow < leny:

            in_range.append(list(rows_prev[ynow])[xnow])
        
    for x in in_range:
        if x == 'L':
            vacant += 1
            n_seats += 1
        if x == '#':
            n_seats += 1
        
    return (vacant, n_seats)
        
rows = open("data", "r").read().split('\n')

rows_prev = rows.copy()
rows_now = rows.copy()

while True:
    for (y, row_p) in zip(range(100), rows_prev):
        if len(row_p) < 5:
            continue
        
        for (x, seat) in zip(range(100), row_p):
            (empty, n_seats) = seat_good(x, y, seat, rows_prev, len(rows), len(rows[0]))

            occupied = n_seats - empty
            #print(f"{y}, {x}  : e = {empty}, n = {n_seats}, o = {occupied}")
            if seat == 'L' and empty == n_seats:
                s = list(rows_now[y])
                s[x] = '#'
                rows_now[y] = "".join(s)
            elif seat == '#' and occupied >= 4:
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
print(table)

final = 0
for c in table:
    if c == '#':
        final += 1

print(final)