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