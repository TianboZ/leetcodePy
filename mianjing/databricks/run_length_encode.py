"""
这道题 我之前刷面经的时候只碰到过一次 就没准备 所以想详细说一下
有两种存储类型，A和B
A：同样的数字，以及这个数字出现的次数，count >= 8才能归于A这个type。比如1出现了5次，是不能算作A的，需要归属于B；但是一直是A的话，count就一直++，只要是大于等于8就可以
B：8个数字，这8个数字是不一样的，可以是[1, 2, 3, 4, 5, 6, 7, 8], 或者[1, 1, 1, 1, 1, 1, 1, 8]
给你一个datastream，对这个stream进行encoding和decoding
class TypeA:
  def __init__(self):
    self.number = None
    self.count = 0

class TypeB:
  def __init__(self):
    self.number = []

class Solution:
  def encoding():
  def decoding():


-----


"""
SIZE = 8

class Solution:
  def add(self, num):
    pass
  def encoding(self, arr:list[int])->str:
    i = 0
    buffer = []
    nums = []  # store B values
    
    while i < len(arr):
      # check if A
      j = i
      while j < len(arr) and arr[j] == arr[i]:
        j += 1
      
      if j - i >= 8:
        # type A
        tmp = 'A' + str(arr[i]) + ':' + str(j - i)    #   A1:8
        buffer.append(tmp)   
        
        i = j
      else:
        if len(nums) == SIZE:
          buffer.append(','.join(nums))     #   e.g.  1,2,3,4,5
          nums = []

        nums.append(str(arr[i]))
        i += 1
    
    # remaing type B
    if nums:
      buffer.append(','.join(nums))

    print('#'.join(buffer))
    return '#'.join(buffer)


  def decoding(self, s: str):
    chunks = s.split('#')
    res = []
    print(chunks)
    for chunk in chunks:
      if chunk[0] == 'A':  #   A1:8
        size = len(chunk)
        # print(chunk[1: size])
        val, count = chunk[1:size].split(':')
        # print(val, count)
        for _ in range(int(count)):
          res.append(int(val))
      else:
        # print(chunk)
        nums = chunk.split(',')
        for n in nums:
          res.append(int(n))

    print(res)


sol  = Solution()
arr = [1,1,1,1,1,1,1,1,      2,3,4,5,6,7,8,9,     10,11,12,13,14,1,1,1,    1]
encoded = sol.encoding(arr)
sol.decoding(encoded)
