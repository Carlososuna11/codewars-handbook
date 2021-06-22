def easyline(n):
    aux=1
    res=0
    for j in range(n+1):
        res+=aux**2
        aux=aux*(n-j)//(j+1)
    return res