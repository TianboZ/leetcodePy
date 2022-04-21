

if 1 < 2 and 2 > 3 : 
  print(True)
else:
  print(False)


s = ' tianbo'
s2 = 'elaine'

def test(s):
  s = 'aa'
  print(s)
  print(s2)

if 1 < 10 and 2 < 10: 
  arr1 = [1, 2]
  arr2 = [1, 2]

  a = '11111111111' if arr1 == arr2 else 3
  # print(a)
  if arr1 == arr2:
    print('arr1 equals to arr2')

  map1 = {a: 1}
  map2 = {a: 1}
  if map1 == map2:
    print('two dict equals')

  str1 = 'a'
  str2 = 'a'
  if str1 == str2:
    print('str1 equals to str2')

test(s)
print(s)