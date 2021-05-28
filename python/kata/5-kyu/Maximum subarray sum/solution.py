def max_sequence(arr):
    return 0 if len(arr)==0 or sum([0 if x <=0 else x for x in arr])==0 else max([elem + sum(arr[index+1:i+1]) for index,elem in enumerate(arr) for i in range(index+1,len(arr))])
  