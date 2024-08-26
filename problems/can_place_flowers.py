class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    cnt = 0
    size= len(flowerbed)
    for i in range(len(flowerbed)):
      if flowerbed[i] == 0:
        prev = i - 1
        next = i + 1
        
        # check left
        if prev >= 0 and flowerbed[prev] == 1:
          continue
        
        # check right
        if next < size and flowerbed[next] == 1:
            continue
        
        flowerbed[i] = 1
        cnt += 1
          
    if cnt >= n:
      print(cnt)
      return True
  
    return False
                