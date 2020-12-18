import time
file = open("data", "r")
lines = file.read().split("\n")
lines.remove('')


def only_parens(line):
    result = [] 
    for (i, char) in enumerate(line):
        if char == '(' or char == ')':
            result.append([char, i])
    return result

def find_simple(parens_locations):
    for i in range(len(parens_locations[:-1])):
        if parens_locations[i][0] == '(' and parens_locations[i+1][0] == ')':
            return [parens_locations[i][1], parens_locations[i+1][1]]
    return [-1, -1]

def eval_simple(subline):
    result = 0
    while True:
        v1_pos = -1
        v2_pos = -1
        v1 = -1
        v2 = -1
        adding = False
        mul = False
        for (i, c) in enumerate(subline):
            if c != '(' and c != ')':
                if c == '+':
                    adding = True
                elif c == '*':
                    mul = True
                else:
                    if v1 != -1:
                        v2 = int(c)
                        v2_pos = i
                        break
                    else:
                        v1 = int(c)
                        v1_pos = i

        if adding:
            evaled = v1 + v2
        if mul:
            evaled = v1 * v2
        subline[v1_pos:v2_pos + 1] = [evaled]
                
        #print(subline)
        if subline[0] == '(':
            if len(subline) == 3:
                return subline[1]
        else:
            if len(subline) == 1:
                return subline[0]   
        #time.sleep(1) 

    return subline[0]

        
def evaluate(line):
    #print(line)
    while True:
        parens_locations = only_parens(line)
        #print(parens_locations)
        if len(parens_locations) < 1:
            break   
        subline_range = find_simple(parens_locations)
        subline = line[subline_range[0]:subline_range[1] + 1]
        #print(subline)
        evaluated = eval_simple(subline)
        #print(evaluated)
        line[subline_range[0]:subline_range[1] + 1] = [evaluated]
        #print(line)

    return eval_simple(line) 


total = 0
for line in lines:
    newline = ""
    prev = '@'
    for c in line:
        if c == ')' or prev == '(':
            newline+=' '
        newline += c
        prev = c

    line = newline.split(" ")
    for (i,c) in enumerate(line):
        if c != '(' and c != ')' and c != '*' and c != '+':
            line[i] = int(c)

    value = evaluate(line)
    total += value

print(total)

file.close()
