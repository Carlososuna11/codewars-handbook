def cakes(recipe, available):
    return min(list(available[key]//recipe[key] if available.get(key) is not None else 0 for key,item in recipe.items()))