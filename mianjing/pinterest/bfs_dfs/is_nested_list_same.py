"""
arr = [1, 2, [3, 4]]
arr2 = [2, 1, [4,3]]

arr and arr2 same, 不考虑order, 只比较内容

"""

arr = [1, 2, [3, [5], 4  ], 'a' ]
arr2 = ['b', 2, [4,3, [5]], 1, 'a' ]

def serialize(arr)->str:
  chunks = []
  
  for ele in arr:
    if isinstance(ele, list):
      chunks.append('[' + serialize(ele) + ']')
    else:
      chunks.append(str(ele))
    
  # print(chunks)
  chunks.sort()
  return ','.join(chunks)
  
def isSame(arr, arr2):
  print(serialize(arr))
  print(serialize(arr2))
  return serialize(arr) == serialize(arr2)

# serialize(arr)
print(isSame(arr, arr2))