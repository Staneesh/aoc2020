file = open("data", "r")
sum = 0
for paragraph in file.read().split("\n\n"):
    buckets = [0] * 26
    for character in paragraph:
        letter_val = ord(character) - ord('a')
        if letter_val >= 0 and letter_val <= 26:
            buckets[letter_val] = 1
    for letter in buckets:
        sum = sum + letter
        
print(sum)
file.close()