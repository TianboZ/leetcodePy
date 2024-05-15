'''

When you evaluate 1 == True, Python compares 1 as an integer with True 
as a boolean, but under the hood, True is treated as its integer
equivalent, which is 1. Therefore, the comparison 1 == True returns
True because both sides of the comparison are effectively the same value (1).

'''
print(1 == True) # true
print(1 is True) # false
print(0 == False) # true


print(2 == True) # false

print(id(True))
print(id(1))
print(id(1))
print(id(2))
print(id(199999))




