from typing import List


class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x:x[0])
    for i in range(len(intervals) - 1):
      r1 = intervals[i]
      r2 = intervals[i + 1]
      if r1[1] > r2[0]:
        return False
        
    return True