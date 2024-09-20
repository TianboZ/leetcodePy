from collections import defaultdict, deque


class Solution:
  def convert(self, rates, toCur, fromCur):
    # build graph
    adj = defaultdict(list) # key: currency, value: [[currency2, rate], ....]
    for a, b, rate in rates:
      adj[a].append([b, rate])
      adj[b].append([a, 1/rate])
    

    print(adj)
    
    # run BFS from to_currency, end at from_currency
    queue = deque([])
    visit = set()
    
    queue.append([toCur, 1])
    visit.add(toCur)
    
    while queue:
      # expand
      curr, rate = queue.popleft()
      print(curr, rate)
      
      if curr == fromCur:
        print(rate)
        break
      
      # generate
      for nei in adj.get(curr, []):
        print(nei)
        curr2, rate2 = nei
        if curr2 not in visit:
          queue.append([curr2, rate * rate2])
          visit.add(curr2)

# test 
rates = [['USD', 'JPY', 110] , ['USD', 'AUD', 1.45],  ['JPY', 'GBP', 0.0070]]
sol = Solution()
sol.convert(rates, 'GBP', 'AUD')

