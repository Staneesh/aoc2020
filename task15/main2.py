file = open("data", "r")
numbers = list(map(int, file.read().replace("\n", "").split(",")))

series = []
ages = [-1] * 50000000

for (i, number) in zip(range(1000), numbers):
    series.append(number)
    ages[number] = i

prev_age = len(numbers)

loops = 30000000
#loops = 2020
#loops = 20
for i in range(len(numbers), loops):
    if i % 100000 == 0:
        print(f"processing {i}...")

    last_spoken = series[-1]


    age = i - prev_age

    #print(f"LS = {last_spoken}, PA = {prev_age}, A = {age}")
    prev_age = ages[age] + 1
    if i >= 3 and ages[age] == -1:
        prev_age = i+1
    #print(f"so now prevage = {prev_age}")
    ages[age] = i
    series.append(age)

#print(series)
print(series[-1])

file.close()
