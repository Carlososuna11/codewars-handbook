def dig_pow(n, p):
    l = [int(str(n)[x])**(p+x) for x in range(len(str(n)))]
    l =sum(l)
    if l % n == 0 :
        return l //n
    return -1