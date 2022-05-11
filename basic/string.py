s1  = 'string111'
print(s1)
print(type(s1))
print(id(s1))
# s1[0] = 1 error, string is immutable!!!

# slicing (substring)
s2 = s1[0:3]
print(s2)
print(id(s2))

# iterating through a string
s3 = 'tianbo111'
for char in s3:
  print(char)
  # print(type(char))

# string to char list
# method1
chars = [c for c in s3]
print(chars)

# method2
chars = list(s3)
print(chars)

# string membership test
if '1' in s3:
  print(s3, 'contains: ', '1')


#  string method: split
s4 = " This will split all words into a list     ".split()
print(s4)


# string method: join
list = ['aaa', '555', 'b']
s5 = ''.join(list) # item in list must be str instance!!!
print(s5)
