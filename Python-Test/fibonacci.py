
def fibo(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

fibo(10)

