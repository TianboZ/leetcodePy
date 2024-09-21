numToEng = {
  1: "One",
  2: "Two",
  3: "Three",
  4: "Four",
  5: "Five",
  6: "Six",
  7: "Seven",
  8: "Eight",
  9: "Nine",
  10: "Ten",
  11: "Eleven",
  12: "Twelve",
  13: "Thirteen",
  14: "Fourteen",
  15: "Fifteen",
  16: "Sixteen",
  17: "Seventeen",
  18: "Eighteen",
  19: "Nineteen",
  20: "Twenty",
  30: "Thirty",
  40: "Forty",
  50: "Fifty",
  60: "Sixty",
  70: "Seventy",
  80: "Eighty",
  90: "Ninety",
  100: "Hundred",
  1000: "Thousand",
  1000000: "Million"
}


class Solution:
  def numberToWords(self, num: int) -> str:
    path = []
    return self.dfs(num, path)
  # recursively build english words, path records english words
  # path: e.g. ['one', 'million', ....]
  
  def dfs(self, num, path)->str:
    # baes case
    if num == 0:
      if len(path) == 0:
        return 'Zero'
      return ' '.join(path)
    
    if num < 20:
      path.append(numToEng[num])
      print(path)
      return ' '.join(path)

    # recursive rule
    if num < 100:
      # 23
      tens = num // 10
      tensInEng = numToEng[tens * 10]
      path.append(tensInEng)
      return self.dfs(num % 10, path)

    if num < 1000:
      # 123
      hundreds = num // 100 # 1
      path.append(numToEng[hundreds])
      path.append('Hundred')

      return self.dfs(num % 100, path)

    if num < 1000000:
      # 123,456
      thous = num // 1000 # 123
      thousInEng = self.dfs(thous, [])
      path.append(thousInEng)
      path.append('Thousand')
      return self.dfs(num % 1000, path)

    if num < 1000000000:
      # 23,456,789
      million = num // 1000000 # 23 
      millionInEng = self.dfs(million, [])
      path.append(millionInEng)
      path.append('Million')
      return self.dfs(num % 1000000, path)

    if num < 1000000000000:
      # 23,456,789
      billion = num // 1000000000 # 23 
      billionInEng = self.dfs(billion, [])
      path.append(billionInEng)
      path.append('Billion')
      return self.dfs(num % 1000000000, path)
