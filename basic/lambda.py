"""

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression

Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

"""

larger = lambda a, b: a if a > b else b

print(larger(1, 10))