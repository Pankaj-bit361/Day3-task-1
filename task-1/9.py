
def fun(n):
    if n<=1:
        return n
    
    else:
        return fun(n-1)+fun(n-2)


def Fibonacci(n):
     series=[]
     for i in range(n):
        series.append(fun(i))
     return fun
   

print(Fibonacci(5))