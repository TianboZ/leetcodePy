# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


"""
soluiton:
- find celebrity candidate
- verify candidate is celebrity 

2 pass array

compleixty:
time O(n)
space O(1)

"""
class Solution:
  def findCelebrity(self, n: int) -> int:
    candidate = 0
    for i in range(1, n):
      if knows(candidate, i):
        candidate = i
    
    for i in range(n):
      if i == candidate:
        continue
      if knows(candidate, i) or not  knows(i, candidate):
        return -1

    return candidate