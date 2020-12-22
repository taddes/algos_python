"""
Interview Question - Integer Reversion

Our task is to design an efficient algorithm to reverse a given integer.
 For example if the input of the algorithm is 1234 then the output should be 4321.
"""

def rev_int(number):
    # Easiest
    num = str(number)[::-1]
    print(num)
    return int(num)
    print(num)

def rev_int2(number):
    num = [num for num in str(number)]
    num = ''.join(num[::-1])
    print(num)
    return int(num)

def rev_int3(number):
    # Overkill
    reversed = ''
    for char in str(number):
        reversed = char + reversed
    print(reversed)
    return int(reversed)

def rev_int4(number):
    # Using modulus and the remainder by dividing by 10
    # Most mathematically sound, as you don't depend on casting to strings
    reversed = 0
    remainder = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        reversed = reversed * 10 + remainder
    print(reversed)
    return reversed


    

rev_int(4568)
rev_int2(456856)
rev_int3(123)
rev_int4(123456789)