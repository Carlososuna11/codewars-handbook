import re
#my code
def calc(expression):
    print(expression)
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
            expression[index+1] = f'-{expression[index+1]}'
        else:
            a.append(value)
    a = ' '.join(a)
    return Calculator().evaluate(a)


#for this kata, I used the solution from https://www.codewars.com/users/jeff1997 of 
# the problem of 'Calculator' https://www.codewars.com/kata/5235c913397cbf2508000048/python 
# which I had already done, just that I noticed that my code passed the test but has an error 
# with the subtraction, so while I refactor my code, I used this person's code
#  | 
#  |
#  |
#  |
#\   /
# \/
class Calculator(object):
    def fuundation_op(self, op, num1, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2

    def priority_level(self, op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 0

    def get_infix_lst(self, strng):
        strng = strng.replace(' ', '')
        # consider whether '-' represents the minus or the operator
        minus_lst = [i for i in re.split(r'(\-\d+\.{0,1}\d*)', strng) if i]
        result = []
        for item in minus_lst:
            if len(result) == 0 and re.search(r'^\-\d+\.{0,1}\d*$', item):
                result.append(item)
                continue
            if len(result) > 0:
                if re.search(r'[\+\-\*\/\(]$', result[-1]):
                    result.append(item)
                    continue
            item_split = [i for i in re.split(r'([\+\-\*\/\(\)])', item) if i]
            result += item_split
        if result[0] == '-':
            result.insert(0, '0')
        return result

    def solve_opreration(self, item, stack1, stack2):
        if len(stack2) == 0:
            stack2.append(item)
        elif stack2[-1] == '(':
            stack2.append(item)
        else:
            a = self.priority_level(item)
            b = self.priority_level(stack2[-1])
            if self.priority_level(item) > self.priority_level(stack2[-1]):
                stack2.append(item)
            else:
                stack1.append(stack2[-1])
                stack2.pop()
                self.solve_opreration(item, stack1, stack2)

    def to_reverse_polish_notation(self, strng):
        infix = self.get_infix_lst(strng)
        stack1 = []
        stack2 = []
        for i, item in enumerate(infix):
            if item in ['+', '-', '*', '/']:
                self.solve_opreration(item, stack1, stack2)
            elif item == '(':
                stack2.append(item)
            elif item == ')':
                if len(stack2) > 0 and '(' in stack2:
                    while stack2[-1] != '(':
                        stack1.append(stack2[-1])
                        stack2.pop()
                    stack2.pop()
            elif re.search(r'^\-?\d+\.?\d*$', item):
                stack1.append(item)
        while len(stack2) > 0:
            stack1.append(stack2[-1])
            stack2.pop()
        return stack1

    def evaluate(self, strng):
        reverse_polish_notation = self.to_reverse_polish_notation(strng)
        result = []
        for item in reverse_polish_notation:
            if item in ['+', '-', '*', '/']:
                num2 = result.pop()
                num1 = result.pop()
                result.append(self.fuundation_op(item, num1, num2))
            else:
                result.append(float(item))
        return result[0]