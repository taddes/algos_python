def fib_iter(n):
    a, b = 0, 1

    while a < n:
        print(a)
        a, b = b, a + b
        
fib_iter(40)