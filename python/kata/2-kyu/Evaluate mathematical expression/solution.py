def calc(expression):
    expression = expression.replace('-',' - ').replace('+',' + ').replace('*',' * ').replace('/',' / ').replace('(',' ( ').replace(')',' ) ').replace('  ',' ').replace('  ',' ').strip().replace(" ",',').split(',')
    convert = {
        '+':'-',
        '-':'+'
    }
    a = []
    for index,value in enumerate(expression):
        if value == '-' and (index==0 or expression[index-1] == '('):
            a.append('0')
            a.append(value)
        elif value == '-' and index>0 and expression[index-1] in ['-','+']:
            a = a[:-1] + [convert[expression[index-1]]]
        elif value == '-' and index>0 and expression[index-1] in ['*']:
            a.append('-1')
            a.append('*')
        elif value == '-' and index>0 and expression[index-1] in ['/']:
            a = a[:-1] + ['*', '-1', '/']
        else:
            a.append(value)
    a = ' '.join(a)
    return Calculator().evaluate(a)


class Calculator(object):
    operations = {
            '+':lambda x,y:x+y,
            '-':lambda x,y:x-y,
            '*':lambda x,y:x*y,
            '/': lambda x,y: x/y,
        }

    def evaluate(self, string):
        calc = string.split(' ')
        divide_multiply = string.count('*') + string.count('/')
        if divide_multiply>0:
            count = 0
            while count < divide_multiply:
                istart = []  # stack of indices of opening parentheses
                b = {}
                for i, c in enumerate(calc):
                    if c == '(':
                        istart.append(i)
                    if c == ')':
                        b[istart.pop()] = i
                auxcont = 0
                for index,i in enumerate(calc):
                    if i in ['/','*']:
                        if count == auxcont:
                            if calc[index+1]=='(':
                                pos = b[index+1]
                                calc = calc[:pos+1] + [')'] + calc[pos+1:]
                            else:
                                calc = calc[:index+2] + [')'] + calc[index+2:]
                            if index == 1:
                                calc = ['(']+calc
                            else:
                                if calc[index-1]==')':
                                    pos =list(b.keys())[list(b.values()).index(index-1)]
                                    calc = calc[:pos] + ['('] + calc[pos:]
                                else:
                                    calc = calc[:index-1] + ['('] + calc[index-1:]
                            break
                        auxcont+=1
                count+=1
        return self.calculate(calc[::-1])

    def calculate(self,calc):
        istart = []  # stack of indices of opening parentheses
        b = {}
        for i, c in enumerate(calc):
            if c == ')':
                istart.append(i)
            if c == '(':
                b[istart.pop()] = i
        if calc[0] == ')':
            index_final = b[0]
            value = self.calculate(calc[1:index_final])
            calc = calc[index_final+1:]
            if len(calc) == 0:
                return value
            else:
                return self.calculate(calc[:])(value)
        elif calc[0] in self.operations:    
            return lambda x: self.operations[calc[0]](self.calculate(calc[1:]),x)
        else:
            value = calc[0]
            calc = calc[1:]
            if '.' in value:
                if len(calc) == 0:
                    return float(value)
                return self.calculate(calc)(float(value))
            else:
                if len(calc) == 0:
                    return int(value)
                return self.calculate(calc)(int(value))