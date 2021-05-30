def driver(data): #["John","James","Smith","01-Jan-2000","M"]
    month = {
        'jan':'01',
        'feb':'02',
        'mar':'03',
        'apr':'04',
        'may':'05',
        'jun':'06',
        'jul':'07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    oneFive = data[2][:5] if len(data[2])>=5 else f"{data[2]}{'9'*(5-len(data[2]))}"
    six = data[3][-2]
    monthData = month[data[3].split('-')[1][:3].lower()]
    sevenEight = monthData if data[4]=='M' else f"{int(monthData[0])+5}{monthData[1]}"
    nineTen = data[3].split('-')[0]
    eleven = data[3].split('-')[2][-1]
    n1213= data[0][0] + '9' if len(data[1])==0 else f"{data[0][0]}{data[1][0]}"
    return f"{oneFive}{six}{sevenEight}{nineTen}{eleven}{n1213}9AA".upper() 