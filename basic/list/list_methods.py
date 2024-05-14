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

# sory 
arr.sort()
print(arr)

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

