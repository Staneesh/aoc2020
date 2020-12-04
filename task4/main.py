file = open("data", "r")

byr = iyr = eyr = hgt = hcl = ecl = pid = 0
good = 0

def is_ok():
    return byr & iyr & eyr & hgt & hcl & ecl & pid

processed = 0
for line in file:
    if len(line) < 2:
        print(f"P:{processed}:byr:{byr}, iyr:{iyr}, eyr:{eyr}, hgt:{hgt}, hcl:{hcl}, ecl:{ecl}, pid:{pid}")
        if is_ok() != 0:
            good = good + 1 
            print(processed)
        byr = iyr = eyr = hgt = hcl = ecl = pid = 0
        processed = processed + 1

    else:
        words = line.split()
        for word in words:
            entry = word[0:3]
            num = word[4:]
            if entry == "hcl":
                if len(num) == 7:
                    hcl = 1
            if entry == "byr" and len(num) == 4:
                if int(num) >= 1920 and int(num) <= 2002:
                    byr = 1
            if entry == "iyr" and len(num) == 4:
                if int(num) >= 2010 and int(num) <= 2020:
                    iyr = 1
            if entry == "eyr" and len(num) == 4:
                if int(num) >= 2020 and int(num) <= 2030:
                    eyr = 1
            if entry == "hgt":
                if num[-2:] == "cm":
                    if int(num[:-2]) >= 150 and int(num[:-2]) <= 193:
                        hgt = 1
                if num[-2:] == "in":
                    if int(num[:-2]) >= 59 and int(num[:-2]) <= 76:
                        hgt = 1
            if entry == "ecl":
                if num == "amb" or num == "blu" or num == "brn" or num == "gry" or num == "grn" or num == "hzl" or num == "oth":
                    ecl = 1
            if entry == "pid":
                if len(num) == 9:
                    pid = 1

print(good)
file.close()