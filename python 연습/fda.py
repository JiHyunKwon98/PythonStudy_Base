def Fibo(n):
    if n<1:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibo(n-2) + Fibo(n-1)
