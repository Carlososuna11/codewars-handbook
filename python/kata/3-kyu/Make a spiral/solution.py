def spiralize(size):
    spiral = [[0 for i in range(size)] for j in range(size)]
    maxWidth = size - 1
    minWidth = 0
    maxHeight = size - 1
    minHeight = 0
    x,y = 0,0
    direction = 'r'
    while True:
        spiral[y][x] =1
        if direction=='r':
            if x<maxWidth:
                x+=1
            elif y+1 <=maxHeight:
                direction = 'd'
                minHeight +=2
            else:
                break
        elif direction=='d':
            if y < maxHeight:
                y+=1
            elif x-1 >minWidth:
                direction = 'l'
                maxWidth-=2
            else:
                break
        elif direction=='l':
            if x>minWidth:
                x-=1
            elif y-1>=minHeight:
                direction='u'
                maxHeight -=2
            else:
                break
        elif direction=='u':
            if y>minHeight:
                y-=1
            elif x+1<maxWidth:
                direction='r'
                minWidth+=2
            else:
                break
    return spiral