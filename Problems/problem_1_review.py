"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
4! = 1 x 2 x 3 x 4 = 24
"""
# from Problems.Solutions.problem_1_review import factorial


# Helper method to test equality
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Create a function that produces the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    out = 1
    # The range() function returns a sequence of numbers, starting from 0 by default,
    # and increments by 1 (by default), and stops before a specified number.
    for i in range(n):
        out = out * (i+1)
    return out




# Todo: Test factorial function
assert_equals(factorial(0), 1)
assert_equals(factorial(3), 6)
assert_equals(factorial(5), 120)


# Todo: Request a number from the user


# Todo: Print a list of factorials from 0 to the given number

