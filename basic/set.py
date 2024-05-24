'''
https://www.geeksforgeeks.org/sets-in-python/
'''
# create a set
set1 = set() # To create an empty set in Python, you should use the set() function. This is because using curly braces {} alone creates an empty dictionary, not a set. Here’s how you do it:
print(type(set1))

# set method: add
set1.add("fff")
set1.add(2)
print(set1)

# set method: pop
# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set. 
set1.pop()
print(set1)





# set method: discard
set1.discard(2999)   # Removes an element from set if it is a member. (Do nothing if the element is not in set)


#   set method: remove
set1.remove(2)   # Removes an element from a set. If the element is not present in the set, raise a KeyError

# check element in set
if "yes" in set1:
  print('yes exist')
else:
  print('yes not exist')


# set metod: clear
set1.clear()
print(set1)



