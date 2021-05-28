def longest_consec(strarr, k):
    output,n = None ,len(strarr)
    if n == 0 or k > n or k<=0 :
        return ""
    for i in range(n-k+1):
        aux = ''
        for j in range(i,i+k):
            aux += strarr[j]
        if output == None or len(output) < len(aux):
            output = aux
    return output