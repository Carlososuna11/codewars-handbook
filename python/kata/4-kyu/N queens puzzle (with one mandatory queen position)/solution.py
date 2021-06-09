conversion ={
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j'
}
conversion_2 = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
}
def queens(position, size):
    solution = queens_algorithm(position,size)
    sol = []
    print(solution)
    for index,value in enumerate(solution):
        if value==9:
            sol.append(f'{conversion[index]}{0}')
        else:
            sol.append(f'{conversion[index]}{value+1}')
    return ','.join(sol)

def queens_algorithm(position,n):
    L = [0 for i in range(n)]
    pos = 9
    if int(position[1])-1 != -1:
        pos = int(position[1])-1
    L[conversion_2[position[0]]] = pos
    stack = [(L,0)] 
    while len(stack) > 0: 
        A,k = stack.pop()
        if k==n:
            k=k-1
            if prometedor(A,k):
                return A
            else:
                break
        else:
            if k != conversion_2[position[0]]:
                for j in range(n):
                    A[k]=j
                    if prometedor(A,k):
                        stack.append((A[:],k+1))
            else:
                if prometedor(A,k):
                    stack.append((A[:],k+1))

def prometedor(A,K):
   for j in range(K):
      if (A[j]==A[K]) or (abs(A[j]-A[K])==abs(K-j)):
         return False