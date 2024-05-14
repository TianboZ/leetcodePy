'''
read 
https://www.freecodecamp.org/news/for-loops-in-python/
https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
'''

# for loop
print('for loop')
arr = [1, 2, 3]
for i in arr:
  print(i)
print('--------')


# iterate over range()
print('iterate over range()')
for i in range(10):
    print(i)  # 0 -> 9
print('--------')


# iterate over range()
print('iterate over list and corresponding index')
A = ["this", "is", "something", "fun"]
for i, word in enumerate(A):
    print(i, word)

'''
If you absolutely need to access the current index of your iteration, 
do NOT use range(len(iterable))! This is an extremely bad practice and
will get you plenty of chuckles from senior Python developers. 
Use the built in function enumerate() instead:
'''
print('--------')



# while loop
print('while loop')
arr = [1, 2, 3]
i = 0
while i < len(arr):
    print(arr[i])
    i += 1
print('--------')



# iterate 2d array
print('iterate 2d array')
m = [[1,2, 9], [3,4,5]]
row = len(m)
col = len(m[0])
for i in range(row):
    for j in range(col):
        print('row:', i, 'col:', j, 'val:' ,m[i][j])

for i, row in enumerate(m):
    for j, val in enumerate(row):
        print('row: ', i, 'col: ', j, 'val:', val)


