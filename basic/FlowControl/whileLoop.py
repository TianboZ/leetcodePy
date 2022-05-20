
from random import random 

i = 0
n = 0
while i < 10:   # 一旦不满足，结束while loop!!!!!!!!
  if random()*10 < 5:
    i += 1
    # n += 1  小心indentation!!!!!!!!!!!!!!!
  n += 1

print(n)
  




