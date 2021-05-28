def validBraces(string):
    while len(string) !=0:
        if '{}' in string or '[]' in string or '()' in string:
            string = string.replace('{}','').replace('()','').replace('[]','')
        else:
            return False
    return True