def corner_fill(square):
    removeStarting = lambda x:  [y[:-1] for y in x[1:]]
    corner = lambda x: x[0]+[y[-1] for y in x[1:]]
    result =[]
    n = len(square)
    if n == 0: return []
    for i in range(n):
        if i % 2 ==0:
            result = result + corner(square)
        else:
            result = result + corner(square)[::-1]
        square = removeStarting(square)
    return result