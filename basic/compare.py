'''

When you evaluate 1 == True, Python compares 1 as an integer with True 
as a boolean, but under the hood, True is treated as its integer
equivalent, which is 1. Therefore, the comparison 1 == True returns
True because both sides of the comparison are effectively the same value (1).

'''
from typing import Counter


print(1 == True) # true
print(1 is True) # false
print(0 == False) # true


print(2 == True) # false

print(id(True))
print(id(1))
print(id(1))
print(id(2))
print(id(199999))

# compare 2 dict
# https://www.geeksforgeeks.org/how-to-compare-two-dictionaries-in-python/
#       == operator used for complare content
map1 = {'a': 1, 'b': 2}
map2 = {'a': 1, 'b': 2}
print('map1 == map2, compare by content', map1 == map2) #  true
print('map1 is map2, compare by reference', map1 is map2) # false


# complare 2 list
arr = [1, 2, 3, 'a']
arr2 = ['a', 1,2 ,3]
print(arr == arr2) # false 

# compare 2 list w/o order
print(Counter(arr) == Counter(arr2)) # true



