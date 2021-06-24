def human_years_cat_years_dog_years(human_years):
    n = human_years
    cats = sum([15 if n>=1 else 0,9 if n-1>=1 else 0]+[4 for i in range(n-2)])
    dogs = sum([15 if n>=1 else 0,9 if n-1>=1 else 0]+[5for i in range(n-2)])
    return [human_years,cats,dogs]