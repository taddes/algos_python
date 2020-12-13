# Tail recursion implementation
# Eliminate dependancy on stack frames. There is no need for back tracking.
# Does not require you to return a value after each function call to pass 
# to next, due to accumulator

def factorial_tail(n, accumulator=1):

    # base case
    if n == 1: 
        return accumulator

    return factorial_tail(n-1, n * accumulator)