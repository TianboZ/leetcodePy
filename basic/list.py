# copy list
a = [1 ,2, 3]
b = a[:] # slicing

print(b)

# list comprehension
aa = [-i for i in a]
print(aa)


# two dimention array
matrix = [[i for i in range(4)] for i in range(3)]
print(matrix)