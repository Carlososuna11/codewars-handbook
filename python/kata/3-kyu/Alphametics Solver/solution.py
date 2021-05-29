def alphametics(puzzle):
    words = puzzle.strip().replace(' ','').replace('=',',').replace('+',',').split(',')
    letters_dict = {}
    unique = ''
    valid =list(map(lambda x: x[0],words))
    usedNumbers = [False,False,False,False,False,False,False,False,False,False]
    for word in words:
        for letter in word:
            if letter not in letters_dict:
                letters_dict[letter] = -1
                unique+=letter
    stack = [(letters_dict,usedNumbers,0)] 
    while len(stack) > 0: 
        letters_dict,usedNumbers,idx = stack.pop()
        if (idx==len(unique)):
            intlist = []
            for word in words:
                num = ''
                for letter in word:
                    num+=str(letters_dict.get(letter,''))
                intlist.append(int(num))
            if(sum(intlist[:-1])==intlist[-1]):
                for key in letters_dict:
                    puzzle = puzzle.replace(key,f"{letters_dict[key]}")
                return puzzle
        else:
            ch = unique[idx]
            for i in [0,1,2,3,4,5,9,8,7,6]:
                if i == 0:
                    if ch in valid:
                        continue
                if usedNumbers[i] == False:
                    usedNumbers[i]=True
                    letters_dict[ch]=i
                    stack.append((letters_dict.copy(),usedNumbers[:],idx+1))
                    usedNumbers[i]=False
                    letters_dict[ch]=-1