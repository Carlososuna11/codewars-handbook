import datetime
def solve_n_queens(n, fixed_queen):
    x,y = fixed_queen[1],fixed_queen[0]
    if n == 1:
        return convert([0])
    if n == 2 or n == 3:
        return None
    if n<= 6:
        sol = less6(x,y,n)
        if sol==None:return None
        return convert(sol)
    if n % 6 != 2 and n % 6 != 3:
        a, b = [i for i in range(2, n+1) if not i % 2], [i for i in range(1, n+1) if i % 2]
    else:
        a, b = [i for i in range(2, n+1) if not i % 2], [i for i in range(1, n+1) if i % 2]
        if n % 6 == 2:
            b = [3, 1] + b[3:] + [5]
        else:
            a = a[1:] + [2]
            b = b[2:] + b[:2]
    sol =  [i-1 for i in a] + [i-1 for i in b]
    pos = sol.index(x)
    op = pos - y
    if op == 0 : return convert(sol)
    cop = sol[:]
    if n%6 in [0,2,3,4]:
        a = perm(sol,x,y,n)
        if a: return a
        if n%6 == 2:
            while True:
                sol = [(i+1)%n for i in cop]
                cop = sol[:]
                a = perm(sol,x,y,n)
                if a: return a
    else:
        if op>0:
            for i in range(op):
                sol.append(sol.pop(0))
        elif op<0:
            for i in range(-1*op):
                sol.insert(0,sol.pop())
        return convert(sol)

def prometedor(A,K):
   for j in range(K):
      if (A[j]==A[K]) or (abs(A[j]-A[K])==abs(K-j)):
         return False
   return True

def convert(sol):
    n = len(sol)
    s = ''
    for i in sol:
        s+=f"{'.'*i}Q{'.'*(n-i-1)}\n"
    return s

def rotate90(a,n):
    for index, value in enumerate(a[:]):
        a[value]=n-1-index
    return a

def less6(x,y,n):
    L = [0 for i in range(n)]
    L[y] = x
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
            if k != y:
                for j in range(n):
                    A[k]=j
                    if prometedor(A,k):
                        stack.append((A[:],k+1))
            else:
                if prometedor(A,k):
                    stack.append((A[:],k+1))

def seed(n):
    L = [0 for i in range(n)]
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
            for j in range(n):
                A[k]=j
                if prometedor(A,k):
                    stack.append((A[:],k+1))

def perm(sol,x,y,n):
    used = []
    stack = [(sol)] 
    while len(stack) > 0:
        sol = stack.pop()
        solutions = [sol]
        if sol not in used:
            used.append(sol)
            for i in range(3):            
                solutions.append(rotate90(solutions[-1][:],n))
                pos = solutions[-1].index(x)
                op = pos - y
                if op == 0: return convert(sol)
                stack.append(solutions[-1])
            for sols in solutions:
                pos = sols[::-1].index(x)
                op = pos-y
                if op == 0: return convert(sols[::-1])
                stack.append(sols[::-1])

print(datetime.datetime.now().strftime("%H:%M:%S"))
a = [6,4,0,2,7,5,3,1]
b = [3,6,2,7,1,4,0,5]
print(rotate90(b,len(b)))
#convert(solve_n_queens(8,(0,3)))
print(datetime.datetime.now().strftime("%H:%M:%S"))

