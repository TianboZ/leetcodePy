class Solution:
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