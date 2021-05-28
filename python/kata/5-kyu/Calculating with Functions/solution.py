calculator = {
    '+': lambda x,y : x+y,
    '-': lambda x,y : x-y,
    '*': lambda x,y : x*y,
    '/': lambda x,y : x//y
}

def zero(op=None):
    if op is None:
        return 0 
    else:
        return calculator[op[0]](0,op[1])

def one(op=None):
    if op is None:
        return 1
    else:
        return calculator[op[0]](1,op[1])

def two(op=None):
    if op is None:
        return 2 
    else:
        return calculator[op[0]](2,op[1])
def three(op=None):
    if op is None:
        return 3
    else:
        return calculator[op[0]](3,op[1])
def four(op=None):
    if op is None:
        return 4
    else:
        return calculator[op[0]](4,op[1])

def five(op=None):
    if op is None:
        return 5
    else:
        return calculator[op[0]](5,op[1])

def six(op=None):
    if op is None:
        return 6
    else:
        return calculator[op[0]](6,op[1])

def seven(op=None):
    if op is None:
        return 7
    else:
        return calculator[op[0]](7,op[1])

def eight(op=None):
    if op is None:
        return 8
    else:
        return calculator[op[0]](8,op[1])

def nine(op=None):
    if op is None:
        return 9
    else:
        return calculator[op[0]](9,op[1])

def plus(n): return ('+',n)
def minus(n): return ('-',n)
def times(n): return ('*',n)
def divided_by(n): return ('/',n)