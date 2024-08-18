"""
10:23 - 10:43


solution:
- ip -> binary 
- binary -> decimal 
- for each CIDR, get it's range, represented in decimal
  - check target ip (in decimal) if in the range
"""

rules = [
	("ALLOW", "192.168.100.0/24"),
	("ALLOW", "192.168.0.5/30"),
	("DENY", "8.8.8.8/0"),
	("ALLOW", "1.2.3.4"),
]


def ipToBin(ip:str)->str:
  chunks = ip.split('.')
  bin = []
  for c in chunks:
    bin.append('{:08b}'.format(int(c)))

  return ''.join(bin)
  print(bin)

# ip: 00000001000000010000000111000000
def binToDec(ip:str)->int: 
  return int(ip, 2)

def isAllowed(ip: str, cidr: str):
  network, prefix = cidr.split('/')
  size = int(prefix)
  networkInBin = ipToBin(network)

  # get range in binary 
  startIpInBin = networkInBin[0: size] + '0' * (32 - size)
  endIpInBin = networkInBin[0: size] + '1' * (32 - size)

  # get range in decimal
  startIpDec = binToDec(startIpInBin)
  endIpDec = binToDec(endIpInBin)
  ipInDec = binToDec(ipToBin(ip))

  print('range:', startIpDec, endIpDec, 'ip:', ipInDec)

  return startIpDec <= ipInDec <= endIpDec




def canAccess(ip):
  for rule in rules:
    action, cidr = rule
    if cidr == ip:
      print(action)
      return
    
    if isAllowed(ip, cidr):
      print(action)
      return
  
  print('no match')


ips = ['192.168.100.1', '8.8.8.8']
for ip in ips:
  canAccess(ip)



