def merge(input1, input2):
  res = []
  i, j = 0, 0
  while i < len(input1) or j < len(input2):
    a = input1[i] if i < len(input1) else None
    b = input2[j] if j < len(input2) else None

    if a and b:
      at, av = a
      bt, bv = b
      if at == bt:
        # If the timestamps are equal, sum the values
        res.append([at, av + bv])
        i += 1
        j += 1
      elif at < bt:
        # If `a`'s timestamp is earlier, add it with b's value
        res.append([at, av + bv])
        i += 1
      else:
        # If `b`'s timestamp is earlier, add it with a's value
        res.append([bt, av + bv])
        j += 1
    elif a:
      # Only `a` remains, add it directly
      res.append(a)
      i += 1
    elif b:
      # Only `b` remains, add it directly
      res.append(b)
      j += 1
  
  return res

list1 = [(1, 3), (3, 1), (5, 3), (6, 4), (10, 1)]
list2 = [(2, 3), (6, 3), (9, 2)]

print(merge(list1, list2))

