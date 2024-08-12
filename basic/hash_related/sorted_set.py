from sortedcontainers import SortedSet

numSet = set([4,4,4,5,1,1,2,3])
numSet.add(5)

ss = SortedSet(numSet)
print(ss)  # [1,2,3,4,5]

#find largest smaller or equal
def findLargestSmallerEqual():
  idx = ss.bisect_right(3.1)
  if idx > 0:
    idx -= 1
    print('index:', idx, 'value:', ss[idx])
  else:
    print('no such value')

  idx = ss.bisect_right(5)
  if idx > 0:
    idx -= 1
    print('index:', idx, 'value:', ss[idx])
  else:
    print('no such value')

  idx = ss.bisect_right(5.1)
  if idx > 0:
    idx -= 1
    print('index:', idx, 'value:', ss[idx])
  else:
    print('no such value')


  idx = ss.bisect_right(0.1)
  if idx > 0:
    idx -= 1
    print('index:', idx, 'value:', ss[idx])
  else:
    print('no such value')


findLargestSmallerEqual()

def findSmallestLarger():
  idx = ss.bisect_right(3.1)
  if idx < len(ss):
    print('target: ', 3.1, 'index:', idx, 'value:', ss[idx])

  idx = ss.bisect_right(4.1)
  if idx < len(ss):
    print('target: ', 4.1, 'index:', idx, 'value:', ss[idx])

  idx = ss.bisect_right(5)
  if idx < len(ss):
    print('target: ', 3.1, 'index:', idx, 'value:', ss[idx])
  else:
    print('no such value')

# findSmallestLarger()


# find smallest larger 