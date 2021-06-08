#https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci#Algref_6
#https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers

def fib(n):
    #F(-n) =(-1)^(n+1)*F(n)
    if n==0: return 0
    neg = False
    if n<0:
        neg = True
        n=-1*n
    i = n-1
    auxOne = 0
    auxTwo = 1
    a,b = auxTwo,auxOne
    c,d = auxOne,auxTwo
    while i>0:
        if i%2!=0:
            auxOne=d*b+c*a
            auxTwo=(d*(b+a)+c*b)
            a,b=auxOne,auxTwo
        auxOne=c**2+d**2
        auxTwo=d*(2*c+d)
        c,d=auxOne,auxTwo
        i=i//2
    if neg==True:
        return -1*(a+b) if (n+1)%2!=0 else a+b
    return a+b