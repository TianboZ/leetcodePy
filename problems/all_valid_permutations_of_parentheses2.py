class Solution(object):
  def validParentheses(self, l, m, n):
    """
    input: int l, int m, int n
    return: string[]
    """
    # write your solution here
    size = (l + m + n) * 2  # ()<>{}
    
    config = {
      "()": [l, 0, 0],  # [total, left cnt, right cnt]
      "<>": [m, 0, 0],
      "{}": [n, 0, 0]
    }
    self.dfs(config, [], size, [])

  def dfs(self, config: dict, path: list, size, openTags: list):
    # base case
    if len(path) == size:
      print(''.join(path))
      return

    # recursive rule
    for k, v in config.items():
      openTag = k[0] # e.g. <
      closeTag = k[1] # e.g. >
      total, left, right = v

      # add open tag
      if left < total:
        path.append(openTag)
        openTags.append(closeTag)  # add close tag, easier to compare later
        v[1] += 1
        self.dfs(config, path, size, openTags)
        path.pop()
        openTags.pop()
        v[1] -= 1

      # add close tag
      if openTags and openTags[-1] == closeTag and right < left:      
        path.append(closeTag)
        openTags.pop() 
        v[2] += 1
        self.dfs(config, path, size, openTags)
        path.pop()
        openTags.append(closeTag)
        v[2] -= 1

sol = Solution()
sol.validParentheses(1, 2, 1)