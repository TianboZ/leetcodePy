import collections

map = {
  'a': 1,
  'b': 2
}

# dynamic key

x = 'dynamic_key'
map[x] = 1

print(map)
print(map.get(x))

# access elememt
print(type(map.get('aa'))) # map['aa'] will throw error if key is not exist! use .get()

# check if exist
if 'a' in map:
  print('a in map')
else:
  print('a is not in map')

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
arr = [1, 2, 2, 2, 'a', 'a']

count = {}
for n in arr:
  tmp = count.get(n, 0) + 1
  count[n] = tmp

print(count)


# build graph
edges = [[1, 2], [3, 4], [5]]   # 0: [1,2], 1: [3,4]  2:[5]


adj = collections.defaultdict(list)
adj[1].append(2)
adj[2].append(1)
print(adj)
print(adj.get(3))


adj2 = collections.defaultdict(set)
adj2[1].add(1)
adj2[1].add(2)
adj2[1].add(2)

print(adj2)
