def valid_parentheses(string):
    string = ''.join(list(filter(lambda x:x=='(' or x==')',list(string.strip()))))
    while len(string) !=0:
        if '()' in string:
            string = string.replace('()','')
        else:
            return False
    return True