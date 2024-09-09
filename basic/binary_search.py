'''
https://docs.python.org/3/library/bisect.html
'''

from bisect import bisect_left, bisect_right


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
      print('index:',i-1, 'val:', a[i - 1])
      return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        print('index:',i, 'val:', a[i])
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        print('index:',i, 'val:', a[i])
        return a[i]
    raise ValueError


# find_le([1,2,3,3], 3)
# find_gt([1,2,3,3,3], 2)
# find_ge([1,2,3,3,3], 2)


arr = [[1, 2], [1, 100], [2, 'a'], [2, 'xx'], [2, -1], [3]]
idx = bisect_right(arr, 3, key=lambda  x:x[0])
if (idx > 0):
    print(idx - 1)

