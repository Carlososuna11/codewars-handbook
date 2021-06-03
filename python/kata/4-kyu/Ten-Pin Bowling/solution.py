def frameValue(value):
    if '/' in value or 'X' in value:
        return 10
    elif len(value)>1:
        return int(value[0])+int(value[1])
    else:
        return int(value)

def bowling_score(frames):
    frames = frames.strip().split(' ')
    result = 0
    if len(frames[-1])>1 or 'X' in frames[-1]:
        last_frame = frames[-1]
        frames = frames[:-1]
        break_poll = False
        value = ''
        for index,i in enumerate(last_frame):
            value+=i
            if i =='X' or i=='/' or index == len(last_frame)-1:
                break_poll = True
            if break_poll:
                frames.append(value)
                value = ''
                break_poll = False
    for index,value in enumerate(frames):
        if value == 'X' and index < 9:
            if len(frames[index+1]) == 1:    
                result += 10 + frameValue(frames[index+1]) + frameValue(frames[index+2][0])
            else:
                result += 10 + frameValue(frames[index+1])
        elif '/' in value and index<9:
            result += 10 + frameValue(frames[index+1][0])
        else:
            result += frameValue(frames[index])
    return result
