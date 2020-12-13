# Factorial example using head recursion
# This stores each function call on the stack as it is head recursion.
# Each function call must be evaluated and returned 

#  n! = n * (n-1)!
def factorial_head(n):
    # base case
    if n == 1: 
        return 1

    # use recursion
    result1 = factorial_head(n - 1)
    result2 = n * result1
    return result2

    # Simple implementation
    # return n * factorial_head(n - 1)


