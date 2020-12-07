file = open("data", "r")

indirect1 = []
indirect2 = []
indirect3 = []
indirect4 = []
indirect5 = []
indirect6 = []
indirect7 = []
indirect8 = []
indirect9 = []
direct = []

for i in range(10):
    file.seek(0)
    for line_ugly in file:
        line = line_ugly[0:-2]
        in_half = line.split("contain")
        if len(in_half) < 2:
            continue
        container = in_half[0].split(' ')
        contained = in_half[1]
        for element in contained.split(','):
            if element[1] == "n":
                print("EMPTY")
            else:
                words = element.split(' ')
                n = int(words[1])

                (word1, word2) = (words[2], words[3])
                if i == 0 and (word1 == "shiny" and word2 == "gold"):
                    direct.append((container[0], container[1]))
                    print(f"{i} container = {container}: {contained.split(',')}")
                if i == 1:
                    for (e1, e2) in direct:
                        if e1 == word1 and e2 == word2:
                            indirect1.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 2:
                    for (e1, e2) in indirect1:
                        if e1 == word1 and e2 == word2:
                            indirect2.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 3:
                    for (e1, e2) in indirect2:
                        if e1 == word1 and e2 == word2:
                            indirect3.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 4:
                    for (e1, e2) in indirect3:
                        if e1 == word1 and e2 == word2:
                            indirect4.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 5:
                    for (e1, e2) in indirect4:
                        if e1 == word1 and e2 == word2:
                            indirect5.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 6:
                    for (e1, e2) in indirect5:
                        if e1 == word1 and e2 == word2:
                            indirect6.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 7:
                    for (e1, e2) in indirect6:
                        if e1 == word1 and e2 == word2:
                            indirect7.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 8:
                    for (e1, e2) in indirect7:
                        if e1 == word1 and e2 == word2:
                            indirect8.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")
                if i == 9:
                    for (e1, e2) in indirect8:
                        if e1 == word1 and e2 == word2:
                            indirect9.append((container[0], container[1]))
                            print(f"{i} container = {container}: {contained.split(',')}")

res = [] 
[res.append(x) for x in direct if x not in res] 
[res.append(x) for x in indirect1 if x not in res] 
[res.append(x) for x in indirect2 if x not in res] 
[res.append(x) for x in indirect3 if x not in res] 
[res.append(x) for x in indirect4 if x not in res] 
[res.append(x) for x in indirect5 if x not in res] 
[res.append(x) for x in indirect6 if x not in res] 
[res.append(x) for x in indirect7 if x not in res] 
[res.append(x) for x in indirect8 if x not in res] 
[res.append(x) for x in indirect9 if x not in res] 
print("RES:")
for (e1, e2) in res:
    print(e1, e2)


print(f"ANS:{len(res)}")
file.close()