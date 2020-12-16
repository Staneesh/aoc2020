def belongs_to(n, interval):
    if n >= interval[0] and n <= interval[1]:
        return True
    return False

file = open("data", "r")

paragraphs = file.read().split("\n\n")

nearby_tickets = paragraphs[2].replace("nearby tickets:\n", "").split("\n")[:-1]
for i in range(len(nearby_tickets)):
    nearby_tickets[i] = list(map(int, nearby_tickets[i].split(",")))

requirements = paragraphs[0].split("\n")
for i in range(len(requirements)):
    requirements[i] = requirements[i].split(": ")[1].split(" or ")
    requirements[i][0] = list(map(int, requirements[i][0].split("-")))
    requirements[i][1] = list(map(int, requirements[i][1].split("-")))

sum_misfits = 0
for (i, ticket) in zip(range(10000), nearby_tickets):
    for number in ticket:
        number_of_matches = 0
        for r in requirements:
            if belongs_to(number, r[0]) == True or belongs_to(number, r[1]) == True:
                number_of_matches += 1
        if number_of_matches == 0:
            #print(f"{i}: number {number} is a misfit.")
            sum_misfits += number

print(sum_misfits)

file.close()
