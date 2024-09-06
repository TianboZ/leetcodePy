
"""
solution:
dyanmic programing

dp[i][j] stores edit distance for subsring of s1[0, i] and substring of s2[0, j]

iterate i
  iterate j
    build dp[i][j]

complexity:
m, n is strings length
time O(m * n)
space O(m * n)

"""
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    # todo: sanity check

    len1 = len(word1)
    len2 = len(word2)

    dp = [[None for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1 + 1):
      for j in range(len2 + 1):
        if i == 0:
          # init 
          dp[i][j] = j
        elif j == 0:
          # init 
          dp[i][j] = i
        elif word1[i - 1] == word2[j - 1]:
          # same char
          dp[i][j] = dp[i - 1][j - 1]
        else:
          # not same 
          dp[i][j] = min(
            dp[i - 1][j - 1] + 1, 
            dp[i - 1][j] + 1, 
            dp[i][j - 1] + 1
          )

    return dp[len1][len2]