import math
file = open("data", "r")

highest_seat = 0
seats=[]

for line in file:
    if len(line) < 3:
        continue

    row = collumn = 0
    
    lo = 0
    hi = 127
    for c in line[0:7]:
        if c == "F":
            hi = math.floor((lo + hi) / 2)
        else: #c == "B"
            lo = math.ceil((lo + hi) / 2)
    row = lo
    
    lo = 0
    hi = 7
    for c in line[7:]:
        if c == "L":
            hi = math.floor((lo + hi) / 2)
        else: #c == "R"
            lo = math.ceil((lo + hi) / 2)
    
    collumn = hi

    seat = row * 8 + collumn
    if line[0:7] == "FBFBBFF":
        print(f"{line[0:7]} - {row}, {line[7:10]} - {collumn} = {seat}")
    highest_seat = max(highest_seat, seat)
    seats.append(seat)
    
print(highest_seat)
present = [0] * 1000
for num in sorted(seats):
    present[num] = num
for (i, num) in zip(range(1000), present):
    if i > 0 and i < 950 and num == 0 and present[i-1] != 0 and present[i+1] != 0:
        print(i)

file.close()