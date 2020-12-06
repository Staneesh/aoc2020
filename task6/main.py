file = open("data", "r")
sum = 0
for paragraph in file.read().split("\n\n"):
    buckets = [0] * 26
    for line in paragraph.split("\n"):
        for character in line:
            letter_val = ord(character) - ord('a')
            if letter_val >= 0 and letter_val <= 26:
                buckets[letter_val] = buckets[letter_val] + 1

    for place in buckets:
        if place == len(paragraph.split("\n")):
            sum = sum + 1      
        
print(sum)
file.close()