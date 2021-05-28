
def solution(args):
    output = ""
    count = 0
    while count < len(args):
        begin = args[count]
        last = args[count]
        pos_count = 0
        count2 = count+1
        while count2 < len(args):
            value = args[count2]
            if value == last+1:
                last = value
                count2 +=1
                count+=1
            else:
                break
        if begin+1==last:
            count-=1
        if begin == last or begin+1==last:
            output+=f"{begin},"
        else:
            output+=f"{begin}-{last},"
        count+=1
    return output[:-1]
