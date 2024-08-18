"""

https://www.geeksforgeeks.org/python-bitwise-operators/
https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/

"""

n = 44

# method 1
print('{:b}'.format(n))   # 1010

"""
{:08b}:

`{}` : This is a placeholder in the format string where the value of i will be inserted.
`:`  : Introduces the formatting specification. What follows : defines how the value should be formatted.
`08` : Specifies that the resulting string should be 8 characters long. If the binary representation of i has fewer than 8 digits, leading zeros will be added to make up the length.
    `0` indicates that leading zeros should be used to fill in any empty spaces.
    `8` specifies the total width (number of characters) of the output.
`b`: Tells Python to format the integer i as a binary number.

"""
print('{0:08b}'.format(n))   # 00101100    8 bit

# method 2
# print(type( bin(44)), bin(44))  # <class 'str'> 0b101100

# method 3
# print(type(format(n, 'b')), format(n, 'b'))  # <class 'str'> 1010

bi = format(n, 'b')
print('bi in string:', bi)
print('bi in num', int(bi))

dec = int(bi, 2)
print('dec:', dec)



a = 10
print(format(a, 'b'))
print('a = 10, a>>1:', a >> 1)

aa = 11
print('aa = 11, aa<<1:', aa << 1)

ip = 100
print('ip: 100, bin:', format(ip, 'b'))   # 1100100   7 bits

def ip_to_bin(ip)->str:
  return "".join(["{:08b}".format(i) for i in map(int, ip.split("."))])

def bin_to_ip(b)->str:
  chunks = []
  for i in range(4):
    j = i * 8
    chunk = int( b[j: j + 8], 2)
    chunks.append(str(chunk))
  return '.'.join(chunks)


bin =ip_to_bin('1.1.10.255')
print(bin)
print(bin_to_ip(bin))



dec = int('00000001000000010000101011111111', 2)
print('dec:', dec)