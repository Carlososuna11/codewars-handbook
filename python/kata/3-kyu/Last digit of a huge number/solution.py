def last_digit(lst):
    if len(lst)==0:
        return 1
    pw = 1
    for i in lst[::-1]:
        pw = i ** (pw if pw < 4 else pw % 4 + 4)
    return pw % 10