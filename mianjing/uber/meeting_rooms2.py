import heapq
from typing import List
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x:x[0]) # sort by start time
    rooms = []  # store end time 
    res = 1
    
    heapq.heappush(rooms, intervals[0][1])

    for i in intervals[1:]:
      if rooms and i[0] >= rooms[0]:
        heapq.heappop(rooms)

      heapq.heappush(rooms, i[1])
      res = max(res, len(rooms))

    return res