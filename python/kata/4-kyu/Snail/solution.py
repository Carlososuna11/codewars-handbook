def snail(snail_map):
    if snail_map == [[]]:
        return []
    state_orientation = {
        0:lambda x: x[0],
        1:lambda x:[i[-1] for i in x],
        2:lambda x: x[-1][::-1],
        3:lambda x: [i[0] for i in x[::-1]]
    }
    remove_orientation = {
        0:lambda x: x[1:],
        1:lambda x:[[j for j in i[:-1]] for i in x],
        2:lambda x: x[:-1],
        3:lambda x: [[j for j in i[1:]] for i in x]
    }   
    count = 0
    l = []
    n = len(snail_map)
    while len(l) < n*n:
        for i in state_orientation[count](snail_map):
            l.append(i)
        snail_map = remove_orientation[count](snail_map)
        count+=1
        count%=4
    return l