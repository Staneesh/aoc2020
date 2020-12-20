import copy
file = open("data", "r")

paragraphs = file.read().split("\n\n")
data = []
for p in paragraphs:
    parts = p.split(":")
    index = int(parts[0][5:])
    image = parts[1].split("\n")
    while "" in image:
        image.remove("")

    for i in range(len(image)):
        image[i] = list(image[i])

    data.append([index, image])

def rotation_right(image):
    result = []
    for i in range(len(image)):
        result.append(['*'] * len(image))

    for (y, line) in enumerate(image):
        for (x, char) in enumerate(line):
            newy = x
            newx = len(image) - y -1
            result[newy][newx] = char
    
    return result

def fliph(image):
    result = []
    for i in range(len(image)):
        result.append(['*'] * len(image))

    for (y, line) in enumerate(image):
        for (x, char) in enumerate(line):
            newy = y
            newx = len(image) - x -1
            result[newy][newx] = char
    
    return result

def flipv(image):
    result = []
    for i in range(len(image)):
        result.append(['*'] * len(image))

    for (y, line) in enumerate(image):
        for (x, char) in enumerate(line):
            newy = len(image) - y - 1 
            newx = x 
            result[newy][newx] = char
    
    return result

def flip_leftup_rightdown(image):
    result = []
    for i in range(len(image)):
        result.append(['*'] * len(image))

    for (y, line) in enumerate(image):
        for (x, char) in enumerate(line):
            newy = x
            newx = y 
            result[newy][newx] = char
    
    return result

def flip_leftdown_rightup(image):
    result = []
    for i in range(len(image)):
        result.append(['*'] * len(image))

    for (y, line) in enumerate(image):
        for (x, char) in enumerate(line):
            newy = len(image) - x - 1
            newx = len(image) - y - 1
            result[newy][newx] = char
    
    return result
    

def pretty_print_image(image):
    image2 = copy.deepcopy(image)
    for line in image2:
        line = "".join(line)
        print(line)

print("before:")
pretty_print_image(data[0][1])

flippedh = flip_leftdown_rightup(data[0][1])
print("after:")
pretty_print_image(flippedh)

file.close()
