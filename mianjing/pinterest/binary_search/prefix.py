words = ['ab', 'app', 'appl', 'apple', 'bbb']


def search(words: list[str], prefix):
  lo = 0
  hi = len(words) - 1
  
  while lo + 1 < hi:
    mid = lo + (hi - lo) // 2
    w = words[mid]
    if w.startswith(prefix):
      hi = mid
    elif w < prefix:
      lo = mid
    else:
      hi = mid
  
  # post check, 2 items remaining
  if words[hi].startswith(prefix):
    return hi
  
  if words[lo].startswith(prefix):
    return lo
  
  return -1

print(search(words, 'b1'))