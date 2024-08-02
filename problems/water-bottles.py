class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

    cnt = 0
    empty = 0
    full = numBottles
    while full + empty >= numExchange:
      cnt += full 
      empty = empty + full
      full = empty // numExchange
      empty = empty % numExchange

    return cnt + full