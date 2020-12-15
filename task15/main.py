file = open("data", "r")
numbers = list(map(int, file.read().replace("\n", "").split(",")))

series = []

def previus_time(n):
    counter = len(series) -1
    for a in reversed(series[:-1]):
        if a == n:
            return counter
        counter -= 1

    return len(series)


for number in numbers:
    series.append(number)

for i in range(len(numbers), 2020):
    if i % 1000 == 0:
        print(f"processing {i}...")
    last_spoken = series[-1]
    age = i - previus_time(last_spoken)
    series.append(age)

print(series[-1])

file.close()
