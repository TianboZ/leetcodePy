# https://leetcode.com/discuss/interview-question/4245529/Pinterest-or-Phone-or-Count-Pins

def getMaxPins(intervals, rangeSize):
  # Sort intervals by their end points
  intervals.sort(key=lambda x: x[1])

  maxCnt = 0
  n = len(intervals)
  
  # Two pointers: sliding window approach
  left = 0
  
  for right in range(n):
    # Move left pointer to ensure the window is within the given range_length
    while intervals[right][1] - intervals[left][0] > rangeSize:
      left += 1

    # Calculate the number of intervals in the current window
    maxCnt = max(maxCnt, right - left + 1)

  return maxCnt

# Example usage:
intervals = [(1, 4, 'l'), (2, 3, 'r'), (4, 8, 'r'), (6, 9, 'l')]
range_length = 5
result = getMaxPins(intervals, range_length)
print(result)  # Expected output: 2