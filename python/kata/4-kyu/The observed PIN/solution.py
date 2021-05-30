
def get_pins(observed:str):
    combos = []
    neighbors = {
		"0": ["8"],
		"1": ["2", "4"],
		"2": ["1", "3", "5"],
		"3": ["2", "6"],
		"4": ["1", "5", "7"],
		"5": ["2", "4", "6", "8"],
		"6": ["3", "5", "9"],
		"7": ["4", "8"],
		"8": ["5", "7", "9", "0"],
		"9": ["6", "8"]
	}
    stack = [(0,'')] 
    idx = 0
    while len(stack) > 0:
        idx,combination = stack.pop()
        digit = observed[idx]
        sols = neighbors[digit][:]
        sols.append(digit)
        for i in sols:
            if idx == (len(observed)-1):
                combos.append(combination+i)
            else:
                stack.append((idx+1,combination+i))
    return combos

    
