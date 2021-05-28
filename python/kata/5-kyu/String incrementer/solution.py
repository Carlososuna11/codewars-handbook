def increment_string(strng):
    str2 = strng[::-1]
    strf = []
    n = []
    flag = True
    for s in str2:
        if s.isnumeric() and flag:
            n.insert(0,s)
        else:
            flag = False
            strf.insert(0,s)
    if len(n) == 0:
        return f'{strng}1'
    else:
        i = -1
        while int(n[i])+1 == 10:
            n[i]='0'
            if len(n) + i == 0:
                n.insert(0,'0')
            i-=1
        n[i]= str(int(n[i])+1)
    return ''.join(strf)+''.join(n)