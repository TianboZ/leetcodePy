import collections

map = {
  'a': 1,
  'b': 2
}

# access elememt
print(type(map.get('aa'))) # map['aa'] will throw error if key is not exist! use .get()

# add or upldate elemnt
map['c'] = 11
print(map)
map['c'] = 12
print(map)


# remove item with key
map.pop('c')
print(map)


# iterate through dict
for e in map.items():
  key, val = e # descturcting
  # print('key: ', e[0])
  # print('val: ', e[1])
  print('key: ', key, 'val: ', val)

for key in map.keys():
  print('key: ', key)


for val in map.values():
  print('val: ', val)


# test if key exist in dict
print('x' in map)
print('a' in map)


# count freqency
list = [1, 2, 2, 2, 'a', 'a']

count = {}
for n in list:
  tmp = count.get(n, 0) + 1
  count[n] = tmp

print(count)



