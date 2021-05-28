def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum([int(x) for x in str(n)]))