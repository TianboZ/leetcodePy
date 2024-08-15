"""
3:34 pm

solution:
- ip -> binary -> decimal 
- each cidr convert to a range, range represented in decimal 
- check if ip in the range j
    - if in the range, return the action: allow or deny


3: 53

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
  for chunk in chunks:
    # chunk
    # print(chunk)
    bin.append("{:08b}".format(int(chunk)))
  return "".join(bin)


# print(ipToBin('1.1.1.192'))

def binToDec(bin:str)->int:
  return int(bin, 2)

# print(binToDec('00000001000000010000000111000000'))

def isIpInRange(ip:str, cidr:str):
  network, prefix = cidr.split('/')
  networkInBin = ipToBin(network)
  prefixLen = int(prefix)

  # get network range in binary 
  startIpInBin = networkInBin[0: prefixLen] + '0' * (32 - prefixLen)
  endIpInBin = networkInBin[0: prefixLen] + '1' * (32 - prefixLen)

  print(startIpInBin, endIpInBin)

  # convert network rang in decimal 
  startIpInDec = binToDec(startIpInBin)
  endIpInDec = binToDec(endIpInBin)
  ipInDec = binToDec(ipToBin(ip))

  print(startIpInDec, endIpInDec,ipInDec )

  return startIpInDec <= ipInDec <= endIpInDec


def canAccess(ip):
  for rule in rules:
    action, cidr = rule
    if cidr == ip:
      return action
    
    if isIpInRange(ip, cidr):
      print(action)
      return action
  
  return False


ips = ['192.168.100.1', '8.8.8.8']
for ip in ips:
  canAccess(ip)