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

def rotations(image):
    result = []

    cur = image
    for i in range(4):
        result.append(cur)
        cur = rotation_right(cur)

    return result

def orientations(image):
    result = []
    for rot in rotations(image):
        result.append(rot)

    result.append(fliph(image))
    result.append(flipv(image))
    result.append(flip_leftdown_rightup(image))
    result.append(flip_leftup_rightdown(image))

    return result

def glues_h(image1, image2):
    edge1 = []
    for (y, line) in enumerate(image1):
        for (x, char) in enumerate(line):
            if y == len(image1) - 1:
                edge1.append(char)

    edge2 = []
    for (y, line) in enumerate(image2):
        for (x, char) in enumerate(line):
            if y == 0:
                edge2.append(char)

    is_same = True
    for (e1, e2) in zip(edge1, edge2):
        if e1 != e2:
            is_same = False
            break
    return is_same

def glues_v(image1, image2):
    edge1 = image1[len(image1)-1]
    edge2 = image2[0] 

    is_same = True
    for (e1, e2) in zip(edge1, edge2):
        if e1 != e2:
            is_same = False
            break

    return is_same

for data_element in data:
    image = data_element[1]
    index = data_element[0]
    
    all_orientations = orientations(image)


    for orientation in all_orientations:
        prev = orientation
        glued_count = 0

        glued_list = [index]
        glued_images_list = [orientation]

        first_image_in_row = orientation 
        for y in range(3):
            for x in range(3):
                if x == 0 and y == 0:
                    continue

                gluing_h = False
                gluing_v = False
                if y == 0:
                    gluing_v = True
                else:
                    gluing_h = True

                for candidate in data:
                    candidate_index = candidate[0]
                    candidate_image = candidate[1]
                    candidate_orientations = orientations(candidate_image)
                    glued = False
                    for candidate_orientation in candidate_orientations:
                        if candidate_index in glued_list:
                            continue

                        if gluing_h:
                            if glues_h(prev, candidate_orientation):
                                if glued_v(glued_images_list[glued_count-2], candidate_orientation):
                                    prev = candidate_orientation
                                    glued_count += 1
                                    glued_list.append(candidate_index)
                                    glued_images_list.append(candidate_orientation)
                                    glued = True
                                    break

                        if gluing_v:
                            if glues_v(first_image_in_row, candidate_orientation):
                                prev = candidate_orientation
                                first_image_in_row = candidate_orientation
                                glued_count += 1
                                glued_list.append(candidate_index)
                                glued_images_list.append(candidate_orientation)
                                glued = True
                                break

                    if glued:
                        print("Glued this:")
                        pretty_print_image(glued_images_list[-1])
                        print("with this as the previous element:")
                        pretty_print_image(orientation)

        #print(glued_count)
        if glued_count == 3 * 3 -1:
            print(glued_list)

print("before:")
pretty_print_image(data[0][1])

flippedh = flip_leftdown_rightup(data[0][1])
print("after:")
pretty_print_image(flippedh)

file.close()
