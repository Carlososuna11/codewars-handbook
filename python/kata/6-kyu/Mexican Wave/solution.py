def wave(people):
    output = []
    for index,elem in enumerate(people):
        if elem != ' ':
            output.append(people[:index] + elem.upper() + people[index+1:])
    return output