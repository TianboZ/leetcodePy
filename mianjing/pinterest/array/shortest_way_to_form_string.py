"""
solution:
xyz -> xz + y + xz

- iterate target
  - iterate source, find the longest substring 

compleixty:
s, t is source and target string length
time O(s * t)
space O(max(s, t))


"""
class Solution:
  def shortestWay(self, source: str, target: str) -> int:
    sourceChars = set(source)
    # check if souce has all char
    for c in target:
      if c not in sourceChars:
        return -1
    
    cnt = 0
    i = 0 # target string index
    while i < len(target):
      # iterate each char in source
      for c in source:
        if i < len(target) and c == target[i]:
          i += 1

      cnt += 1

    print(cnt)
    return cnt