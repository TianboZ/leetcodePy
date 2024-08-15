import ipaddress
from turtle import circle

# Define the CIDR block
cidr_block = '192.168.1.0/24'


# # Create an IP network object
# network = ipaddress.IPv4Network(cidr_block, strict=False)

# # Get the first (network) and last (broadcast) IP addresses
# first_ip = int(network.network_address)
# last_ip = int(network.broadcast_address)

# # Convert the IPs back to decimal
# first_ip_decimal = first_ip
# last_ip_decimal = last_ip

# # Convert the IPs to dotted decimal format for display
# first_ip_str = str(ipaddress.IPv4Address(first_ip_decimal))
# last_ip_str = str(ipaddress.IPv4Address(last_ip_decimal))

# # Print results
# print(f"CIDR Block: {cidr_block}")
# print(f"First IP: {first_ip_str} (Decimal: {first_ip_decimal})")
# print(f"Last IP: {last_ip_str} (Decimal: {last_ip_decimal})")

# # Calculate the total number of IP addresses in the range
# total_ips = last_ip - first_ip + 1
# print(f"Total IP addresses: {total_ips}")


def ip_to_bin(ip)->str:
  return "".join(["{:08b}".format(i) for i in map(int, ip.split("."))])

def bin_to_ip(b)->str:
  chunks = []
  for i in range(4):
    j = i * 8
    chunk = int( b[j: j + 8], 2)
    chunks.append(str(chunk))
  return '.'.join(chunks)

def bin_to_dec(bin: str)->int:
  return int(bin, 2)

# bin = ip_to_bin('1.1.10.255')
# print(bin)
# print(bin_to_ip(bin))

def isInRange(ip: str, cidr: str):
  ipInBin = ip_to_bin(ip)
  networkIp, prefix = cidr.split('/')
  prefixLen = int(prefix)
  networkInBin = ip_to_bin(networkIp)
  
  # find ip range in binary 
  startIpInBin = networkInBin[0: prefixLen] + '0' * (32 - prefixLen)
  endIpInBin = networkInBin[0: prefixLen] + '1' * (32 - prefixLen)

  # convert startIpInBin,endIpInBin, ip into decimal 
  startIpInDec = bin_to_dec(startIpInBin) 
  endIpInDec = bin_to_dec(endIpInBin)
  ipInDec = bin_to_dec(ipInBin)

  return startIpInDec<= ipInDec <= endIpInDec

cidr = '192.168.100.0/24'
ip = '192.168.100.1'
ip2 = '192.168.2.10'

# print(isInRange(ip, cidr))
# print(isInRange(ip2, cidr))

rules = [
	("ALLOW", "192.168.100.0/24"),
	("ALLOW", "192.168.0.5/30"),
	("DENY", "8.8.8.8/0"),
	("ALLOW", "1.2.3.4"),
]

rules2 = [
	("ALLOW", "192.168.0.1/32"),
	("DENY", "192.168.0.4/30"),
]

def access_ok(ip):
  map = {
    'ALLOW': True,
    'DENY': False
  }
  for rule in rules:
    action, cidr = rule

    if cidr == ip:
      return map.get(action)

    if isInRange(ip, cidr):
      print('ip:', ip, ' cidr:', cidr)
      print(action)
      return map.get(action)

  print('fallback')
  return False


print(access_ok('192.168.100.1'))
print(access_ok('8.8.8.8'))
print(access_ok('192.168.0.7'))