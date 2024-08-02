from typing import List


class Solution:
  def ipToCIDR(self, ip: str, n: int) -> List[str]:
    def binToDec(bin):
      pass

def ip_to_bin(ip):
  return "".join(["{:08b}".format(i) for i in map(int, ip.split("."))])

def bin_to_ip(b):
  return ".".join([str(int(b[i:i+8],2)) for i in range(0, 32, 8)])
      

bi = ip_to_bin('192.0.2.0')
print(bi)
ip = bin_to_ip(bi)
print(ip)


# def ip_to_int(ip):
#   ans = 0
#   for x in ip.split('.'):
#     ans = 256 * ans + int(x)
#   return ans

# def int_to_ip(x):
#   return ".".join(str((x >> i) % 256) for i in (24, 16, 8, 0))

# bi2 = ip_to_int('192.0.2.0')
# print(bi2)