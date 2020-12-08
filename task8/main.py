file = open("data", "r")

result = 0
lines_original = file.read().split('\n')
line = lines_original[0]
to_change = 0

while True:
    lines = lines_original.copy()
    acc = 0
    visited = [0] * 1000
    cur_line = 0    
    
    if result != 0:
        break
    
    print(f"Trying {to_change}")

    while True:
        if cur_line == len(lines):
            result = acc
            break
        if visited[cur_line] == 1:
            break

        visited[cur_line] = 1
        line = lines[cur_line]
        words = line.split(' ')

        instruction = words[0]
        if cur_line == to_change:
            if instruction == "nop":
                instruction = "jmp"
            if instruction == "jmp":
                instruction = "nop"
            if instruction == "acc":
                break

        if instruction == "nop":
            cur_line = cur_line + 1
        else:
            
            val = int(words[1])
            if instruction == "acc":
                acc = acc + val
                cur_line = cur_line + 1
            else:
                cur_line = cur_line + val
    
    to_change += 1
            

print(result)

file.close()