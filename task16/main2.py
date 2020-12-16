import itertools

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

my_ticket = list(map(int, paragraphs[1].replace("your ticket:\n", "").replace("\n", "").split(",")))

valid_tickets = []
for (i, ticket) in zip(range(1000), nearby_tickets):
    numbers_with_a_match = 0
    if len(ticket) < 2:
        continue
    #print(i, ticket)
    for number in ticket:
        number_of_matches = 0
        for r in requirements:
            if belongs_to(number, r[0]) == True or belongs_to(number, r[1]) == True:
                number_of_matches += 1
        if number_of_matches != 0:
            numbers_with_a_match += 1

    if numbers_with_a_match == len(requirements):
        valid_tickets.append(ticket)

if 0:
#print(valid_tickets)

#requirements_permutations = list(itertools.permutations(range(6)))
#print(requirements_permutations)
    dep_len = 6
    departure_combinations = list(itertools.combinations(range(len(requirements)), dep_len))
    print(len(departure_combinations))

    true_permutation = []
    for combination in departure_combinations:
        tickets_matched_this_combination = 0
        #print(f"checking combination {combination}")
        for ticket in valid_tickets:
            requirements_satisfied = 0
            for (i, j) in zip(combination, range(20)):
                number = ticket[i]
                requirement = requirements[j]
                #print(f"n = {number}, r = {requirement}")
                if belongs_to(number, requirement[0]) == True or belongs_to(number, requirement[1]) == True:
                    requirements_satisfied += 1
            #print(f"requirements_satisfied = {requirements_satisfied}")
            if requirements_satisfied == dep_len:
                tickets_matched_this_combination += 1

        if tickets_matched_this_combination == len(valid_tickets):
            true_permutation = combination
            break   

    print(true_permutation)

true_permutation = [1, 3, 6, 8,9,10]

better = 0
for ticket in valid_tickets:
    good = 0
    for (i, j) in zip(true_permutation, range(1000)):
        number = ticket[i]
        requirement = requirements[j]
        if belongs_to(number, requirement[0]) == True or belongs_to(number, requirement[1]) == True:
            good += 1
         
    if good == len(true_permutation):
        better += 1
print(len(nearby_tickets), len(valid_tickets), better)

print(my_ticket)
prod_departures = 1
for (i, j) in zip(true_permutation, range(100)):
    print(my_ticket[i])
    print(requirements[j])
    prod_departures *= my_ticket[i]

print(prod_departures)

file.close()
