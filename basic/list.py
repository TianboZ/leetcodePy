# copy list
a = [1 ,2, 3]
b = a[:] # slicing

print(b)

# list comprehension
aa = [-i for i in a]
print(aa)

aa.append('5')


# two dimention array
matrix = [[i for i in range(4)] for i in range(3)]
print(matrix)
print(matrix[0][1])


# buid in method
arr = list('aaa')
print(arr)



arr = list((1,2,3))
print(arr)



arr = list({1,1,1,1,2}) # set
print(arr)

arr = list({'aa': 1, 'bb': 2, 'cc': 33}) # set
print(arr)


# list methods
arr = []
arr.append(100)
print(arr)
