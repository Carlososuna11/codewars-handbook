def create_multiplications(n):
    return [lambda x ,i=i: x*i for i in range(n)]