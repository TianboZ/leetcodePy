from sortedcontainers import SortedDict

class TimeMap:
  def __init__(self):
    self.map = {}  # <key: <time: value>>

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.map:
      sd = SortedDict()
      self.map[key] = sd
      self.map[key][timestamp] = value
    else:
      self.map[key][timestamp] = value

  def get(self, key: str, timestamp: int) -> str:
    if key not in self.map:
      return ""
    else:
      if timestamp in self.map[key]:
        return self.map[key][timestamp]
      else:
        sd: SortedDict = self.map[key]
        prevTimeIdx = sd.bisect_right(timestamp)
        if prevTimeIdx > 0:
          prevTimeIdx -= 1
          k, v = sd.peekitem(prevTimeIdx)
          return v

        return ""
