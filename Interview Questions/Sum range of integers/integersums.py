# integersums.py
""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""

def add_it_up(n):
    """
        Function that adds up all numbers from zero to n, n being the passed
        in argument.
    """
    if type(n) != int:
        print(f'Invalid. Must pass in number. {type(n)} invalid')
        return 0

    total = sum([num for num in range(0, n+1)])
    return total


print(add_it_up(3))

def add_alt1(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum

def add_alt2(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

def add_alt3(n):
    return sum(range(n + 1))