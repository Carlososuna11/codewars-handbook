def decode(s):
    dec = dict()
    def dec_pos(x,e):
        for i in range(x+1):
            e=dec[e]
        return e
    for i in range(32,127):
        dec[encode(chr(i))] = chr(i) 
    a=''
    for index,value in enumerate(s):
        a+=dec_pos(index,value)
    return a