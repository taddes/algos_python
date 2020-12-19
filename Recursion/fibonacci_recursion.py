def fib_head(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # make recursive function calls
    # Multiple stack frames with teh same value
    fib1 = fib_head(n - 1)
    fib2 = fib_head(n - 2)

    # summation operation
    result = fib1 + fib2
    
    return result

def fib_tail(n, a=0, b=1):

    if n == 0:
        return a 
    if n == 1:
        return b

    return fib_tail(n-1, b, a+b)