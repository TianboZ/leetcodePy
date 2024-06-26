
"""

 TypeError: unhashable type: 'list'
 https://rollbar.com/blog/handling-unhashable-type-list-exceptions/
 set element, dict key, must be hashable object. list is not hashable

In Python, for two objects to be considered the same (or unique) in a set or as keys in a dictionary, they must:

1. Have the same hash value: The __hash__ method must return the same value for both objects.
2. Be considered equal: The __eq__ method must return True when comparing the two objects.

Explanation
- Hash Value: The __hash__ method is used to quickly narrow down potential matches in the hash table.
- Equality Check: Once potential matches are found (those with the same hash value), the __eq__ method is used to confirm if the objects are truly equal.

"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = n2

print(hash(n1))
print(hash(n2))
print(n1 == n2) # false, they are differernt object

set1 = set()
set1.add(n1)
set1.add(n2)
set1.add(n3)

print(set1)  # 2 itmes
print(len(set1))   # 2

print('----Objects with Same Hash and Equality--------')
class TreeNodeWithCustomHashFunction:
    def __init__(self, val):
        self.val = val

    def __hash__(self) -> int:
        # return self.val
        return 1111

    def __eq__(self, other):
        if isinstance(other, TreeNodeWithCustomHashFunction):
            return self.val == other.val
        return False

# Objects with the same hash but different values
m1 = TreeNodeWithCustomHashFunction(1)
m2 = TreeNodeWithCustomHashFunction(12)
s4 = set()
s4.add(m1)
s4.add(m2)
print(s4)  # Output: 2 because their 'val' attributes are different


print('---- Objects with Same Hash and Forced Equality--------')

class ClassWithHashAndEq:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  # how to customize hash function
  def __hash__(self) -> int:
    return 100

  def __eq__(self, other) -> bool:
    return True

m1 = ClassWithHashAndEq(1)
m2 = ClassWithHashAndEq(12)
print(hash(m1), hash(m2))
print(m1 == m2) # true, they are differernt object
set3 = set()
set3.add(m1)
set3.add(m2)
print(set3) # size 1, because __eq__ always returns True