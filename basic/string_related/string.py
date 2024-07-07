s1  = 'string111'
print(s1)
print(type(s1))
print(id(s1))
# s1[0] = 1 error, string is immutable!!!

# slicing (substring)
s2 = s1[0:3]
print(s2)
print(id(s2))


# access letter via index
print(s1[4])

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


# join
list = ['aaa', '555', 'b']
s5 = ''.join(list) # item in list must be str instance!!!
print(s5)


# split
text= 'Love thy      neighbor        '
print(text.split()) # splits at space
grocery = 'Milk, Chicken, Bread'
print(grocery.split(',')) # splits at ','
print(grocery.split(':')) # Splits at ':'

# strip
text = '   a bb    '
print(text.strip())
print('length is: ', len(text.strip())) # 4

# check string is number
txt = "565543 " # false
x = txt.isnumeric()

print(x)

# ASCII a=97
letters = [chr(i) for i in range(97, 97 + 26)]
print(letters)


ssss = '12345'
for i in ssss:
  print(i)

#check if a string is substring 
# https://www.geeksforgeeks.org/check-if-string-contains-substring-in-python/
print('tianbo' in 'tianbo1')