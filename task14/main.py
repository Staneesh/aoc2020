file = open("data", "r")

lines = file.read().split('\n')
mask = 0
memory = []

def find_mem(val):
    for (m, v) in memory:
        if m == val:
            return True
    return False

def replace_mem(ma, value):
    for i in range(len(memory)):
        if memory[i][0] == ma:
            memory[i][1] = value
            break

def find_masks(mem_index, mask_og):

    mask_l = [0] * 36
    for i in range(36):
        digit = (mem_index >> i)%2
        mask_index = 35-i
        mask_char = mask_og[mask_index]

        if mask_char == 'X':
            mask_l[mask_index] = 'X'
        elif mask_char == '1':
            mask_l[mask_index] = '1'
        else:
            mask_l[mask_index] = str(digit)

    mask = "".join(mask_l)
    #print(f"mask = {mask}")

    xs = [0]*36
    n_x = 0
    xs_pos = []
    addresses = []

    for i in range(36):
        mask_index = 35-i
        if mask[mask_index] == 'X':
            xs[mask_index] = 1
            xs_pos.append(i)
            n_x += 1

    for i in range(1<<n_x):
        places = []
        for j in range(n_x):
            place_lit = (i >> j)%2
            if place_lit == 1:
                places.append(xs_pos[j])
        
        changed_mask = mask.replace('X', '0')

        for place in places:
            l = list(changed_mask)
            l[35-place] = '1'
            changed_mask = "".join(l)

        #print(changed_mask)
        this_address = 0
        for j in range(36):
            mask_index = 35 - j
            this_address += int(changed_mask[mask_index]) << j

        addresses.append(this_address)
    
    return addresses

for (i, line) in zip(range(1000), lines):
    if len(line) < 3:
        continue

    if line.find("mask") != -1:
        mask = line.split(' ')[2]
        continue

    closing_index = line.find(']')
    mem_index = int(line[4:closing_index])
    value = int(line.split(' ')[2])

    if value == 0:
        continue

    print(f"processing {i}...")
    addresses = find_masks(mem_index, mask)
    for ma in addresses:
        if find_mem(ma) == False:
            memory.append([ma, value])
        else:
            replace_mem(ma, value)
    

result = 0
for (me, v) in memory:
    result += v

print(result)

file.close()