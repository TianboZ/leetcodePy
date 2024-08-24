arr = [1, 2, 3]

# length
print('len(): ', len(arr))

# append to tail
arr.append(4)
print(arr)

# pop
arr.pop()
print(arr)

# reverse
arr.reverse()
print(arr)

# sorting
arr.sort()
print(arr)

# https://www.freecodecamp.org/news/lambda-sort-list-in-python/#heading-what-is-a-lambda-function
my_list = [('tianbo', 100), ('cherry', 1), ('apple', 3), ('banana', 2),  ]

# Sort by the second element of each tuple
my_list.sort(key=lambda x: x[1])
print(my_list)

# shallow copy array
arr.append({'a': 1})
arr2 = arr.copy()
dict_in_arr2 = arr[3]
print(dict_in_arr2)
dict_in_arr2['a'] = 200
print(arr)

# using slicing
arr3 = arr2[:]
print(arr3)


# deep copy array

# unpack
a, b, c = [1,2,3]
print('a=', c, 'b=', b, 'c=', c)


# contains
arr = [1,2,3]
if 1 in arr: 
  print('1 in [1,2,3]') # 1 in [1,2,3]