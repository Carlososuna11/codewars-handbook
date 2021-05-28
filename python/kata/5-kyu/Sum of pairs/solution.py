def sum_pairs(lst, s):
    aux = {}
    for i in lst:
        if aux.get(s-i) != None:
            return [s-i,i]
        aux[i]=True
    return None