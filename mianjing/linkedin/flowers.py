'''
[1,  0 , 0 , 0， 1 , 0,  0,  0 ]

1: flower
0: 花盆
要求花不能挨着

posible solution 
        |                |
index   2                6

'''
from typing import List, Dict


class Solution:
  # dont modify original array
  # time O(n)  space O(n)    n is length of input
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    oldFlowerIdx = []
    newFlowerIdx = [] 
    for i, ele in enumerate(flowerbed):
      if ele == 1:
        oldFlowerIdx.append(i)
        newFlowerIdx.append(i)
        continue
      if ele == 0:
        # check prev
        prev = i - 1
        if prev >= 0 and flowerbed[prev] == 1:
          continue
        if newFlowerIdx and newFlowerIdx[-1] == prev:
          continue

        # check next
        next = i + 1
        if next < len(flowerbed):
          if flowerbed[next] == 1:
            continue
        
        newFlowerIdx.append(i)
        
    # print(oldFlowerIdx, newFlowerIdx)
    if len(newFlowerIdx) - len(oldFlowerIdx) >= n:
      return True
    return False
  
  def canPlaceFlowers2(self, flowerbed: List[int], n: int) -> bool:
    oldCnt = 0
    newFlowerIdx = []

    for i, ele in enumerate(flowerbed):
      if ele == 1:
        oldCnt += 1
        newFlowerIdx.append(i)
        continue
      else:
        # check prev
        prev = i - 1
        if prev >= 0 and flowerbed[prev] == 1:
          continue
        
        if newFlowerIdx and newFlowerIdx[-1] == prev:
          continue

        # check right
        next = i + 1
        if next < len(flowerbed) and flowerbed[next] == 1:
          continue

        newFlowerIdx.append(i)
    
    return len(newFlowerIdx) - oldCnt > n








