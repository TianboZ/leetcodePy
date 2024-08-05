"""
what lib i can use?
https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages

Using Python3 SortedDict Effectively in LC
https://leetcode.com/discuss/study-guide/1515408/using-python3-sorteddict-effectively-floor-ceillings-minimum-maximum-etc
"""

from sortedcontainers import SortedDict

map = SortedDict({1:1, 2:2, 3:3})
print(map)


def findLargestSmallerEqual(target):
  index = map.bisect_right(target)
  # Adjust index to get the largest smaller or equal value
  if index > 0:
    index -= 1
    key, value = map.peekitem(index)  # Get the key at that index
    print(f"The largest smaller or equal value to {target} is {value}, index={index}")
  else:
    print(f"No value smaller or equal to {target} found.")


target = 0.1
findLargestSmallerEqual(target)

target = 2.5
findLargestSmallerEqual(target)

target = 4  # 4 is larger than all values
findLargestSmallerEqual(target)



def findSmallestLarger(target):
  index = map.bisect_right(target)
  # Adjust index to get the largest smaller or equal value
  if index < len(map):
    key, value = map.peekitem(index)  # Get the key at that index
    print(f"The smallest larger value than {target} is {value}, index={index}")
  else:
    print(f"No value larger than {target} found.")

target = 2.9
# findSmallestLarger(target)