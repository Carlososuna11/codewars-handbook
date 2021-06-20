def quarter_of(month):
    quarter = {
        3:1,
        6:2,
        9:3,
        12:4
    }
    for key,value in quarter.items():
        if month <=key:
            return value
    raise ValueError(month,'this Month does not exists')