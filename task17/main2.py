file = open("data", "r")

rows = file.read().split("\n")[:-1]
coords = []
cycles = 6

def find_neighbors(coord):
    active_neighbors = []
    inactive_neighbors = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    looking_at = []
                    looking_at.append(coord[0] + dx)
                    looking_at.append(coord[1] + dy)
                    looking_at.append(coord[2] + dz)
                    looking_at.append(coord[3] + dw)

                    if looking_at in coords:
                        active_neighbors.append(looking_at)
                    else:
                        inactive_neighbors.append(looking_at)

    return (active_neighbors, inactive_neighbors)


def evolve():
    inactive_total = []
    
    coords_to_remove = []
    for coord in coords:
        (active_neighbors, inactive_neighbors) = find_neighbors(coord)  
        active_count = len(active_neighbors)
        if active_count != 2 and active_count != 3:
            if not coord in coords_to_remove:
                coords_to_remove.append(coord)
        for inactive in inactive_neighbors:
            inactive_total.append(inactive)
    
    inactive_processed = []
    mapped = []
    for inactive in inactive_total:
        if not inactive in inactive_processed:
            inactive_processed.append(inactive)
            mapped.append([inactive, inactive_total.count(inactive)])
    
    for c in coords_to_remove:
        coords.remove(c)

    #print(mapped)
    for e in mapped:
        if e[1] == 3:
            coords.append(e[0])

def count_active():
    return len(coords)

for (y, row) in enumerate(rows):
    for (x, character) in enumerate(row):
        if character == '#':
            coords.append([x, y, 0, 0])

print(count_active())
for cycle in range(cycles):
    evolve()
    print(count_active())

    
    

file.close()
