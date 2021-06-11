def sort_array(source_array):
    aux = iter(sorted([i for i in source_array if i%2!=0]))
    return [next(aux) if i%2!=0 else i for i in source_array]