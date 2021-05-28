def delete_nth(order,max_e):
    output = []
    for elem in order:
        if output.count(elem) <max_e:
            output.append(elem)
    return output