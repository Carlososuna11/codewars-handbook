def nQueen(n):
    rs = [0 for i in range(n)]
    if n in [2,3]: return []
    k=0
    if n%6==2 :
        for i in range(2,n+1,2) :
            rs[k]=i-1
            k+=1
        rs[k]=3-1
        k+=1
        rs[k]=1-1
        k+=1
        for i in range(7,n+1,2) :
            rs[k]=i-1
            k+=1
        rs[k]=5-1
    elif n%6==3 :
        rs[k]=4-1
        k+=1
        for i in range(6,n+1,2) :
            rs[k]=i-1
            k+=1
        rs[k]=2-1
        k+=1
        for i in range(5,n+1,2) :
            rs[k]=i-1
            k+=1
        rs[k]=1-1
        k+=1
        rs[k]=3-1
    else :
        for i in range(2,n+1,2) :
            rs[k]=i-1
            k+=1
        for i in range(1,n+1,2) :
            rs[k]=i-1
            k+=1
    return rs