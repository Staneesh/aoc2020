file = open("data", "r")

nums = []
result = 0
special = 14360655
lines = file.read().split('\n')[:-1]

for (i, line) in zip(range(10000), lines):

    new_num = int(line)

    #print(f"i = {i}: {nums}, new_num = {new_num}")

    total = 0
    for n1 in range(i, len(lines)):
        total += int(lines[n1])
        if total == special:
            a2 = int(lines[n1])
            print(i, n1)
            result = new_num + a2
            break

    if result != 0:
        break


print(result)

check = 0
for i in range(390, 406 +1):
    check += int(lines[i])
print(check)

smol = 100000000
big = -1

for i in range(390, 406 + 1):
    val = int(lines[i])
    if val > big:
        big = val
    if val < smol:
        smol = val

print(smol, big, smol+ big)

file.close()
