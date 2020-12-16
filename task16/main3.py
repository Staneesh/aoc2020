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

valid_tickets = []
for (i, ticket) in zip(range(1000), nearby_tickets):
    numbers_with_a_match = 0
    if len(ticket) < 2:
        continue
    for number in ticket:
        number_of_matches = 0
        for r in requirements:
            if belongs_to(number, r[0]) == True or belongs_to(number, r[1]) == True:
                number_of_matches += 1
        if number_of_matches != 0:
            numbers_with_a_match += 1

    if numbers_with_a_match == len(requirements):
        valid_tickets.append(ticket)

sudoku = []
for i in range(len(requirements)):
    sudoku.append([1] * len(requirements))
print(sudoku)

for collumn in range(len(requirements)):
    for (ri, r) in enumerate(requirements):
        for (ti, ticket) in enumerate(valid_tickets):
            number = ticket[collumn]
            print(f"processing number {number}")
            if belongs_to(number, r[0]) == False and belongs_to(number, r[1]) == False:
                sudoku[ri][collumn] = 0
                print(f"number {number} does not fit requirements {r} at index {ri}, collumn = {collumn}")
                print(sudoku)

        
print(sudoku)

collumns_processed = []

def find_determined_collumn():
    ri_res = 0
    for collumn in range(len(valid_tickets)):
        if collumn in collumns_processed:
            continue
        ones = 0
        for (ri, r) in enumerate(requirements):
            if sudoku[ri][collumn] == 1:
                ones += 1
                ri_res = ri

        if ones == 1:
            collumns_processed.append(collumn)
            return (collumn, ri_res)

def count_ones():
    ones = 0
    for collumn in range(len(requirements)):
        for (ri, r) in enumerate(requirements):
            ones += sudoku[ri][collumn]
    return ones

while count_ones() != len(requirements):
    (c, ri) = find_determined_collumn()
    print(c, ri)
    for ci in range(len(requirements)):
        if c != ci:
            sudoku[ri][ci] = 0

print(sudoku)

my_ticket = list(map(int, paragraphs[1].replace("your ticket:\n", "").replace("\n", "").split(",")))

result = 1
for ri in range(6):
    for collumn in range(len(requirements)):
        if sudoku[ri][collumn] == 1:
            result *= my_ticket[collumn]

print(result)

file.close()
