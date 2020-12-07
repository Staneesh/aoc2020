file = open("data", "r")


result = 0

def count_bags(start1, start2, depth):
    file.seek(0)
    if depth > 10:
        return 0
    
    #global result
    result = 0
    for line in file:
        in_half = line.split("contain")
        if len(in_half) < 2:
            return 0
        container = in_half[0].split(' ')
        (what1, what2) = (container[0], container[1])
        contained = in_half[1]

        if start1 == what1 and start2 == what2:
            for element in contained.split(','):
                if element[1] == "n":
                    print(f"container = {container}: {contained.split(',')}")
                    return 0
                else:
                    words = element.split(' ')
                    n = int(words[1])
                    (word1, word2) = (words[2], words[3])
 
                    print(f"container = {container}: {contained.split(',')}")
               
                    result  = result + n + n * count_bags(word1, word2, depth + 1)
            
            print(result)
            return result


result = count_bags("shiny", "gold", 0)
print(f"ANS:{result}")
file.close()