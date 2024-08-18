from typing import List

DE = '##'   # delimiter
ORI = '#'   # original char
ENCODE = "#/"

class Codec:
  
  def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    res = []
    for s in strs:
      s = s.replace(ORI, ENCODE)
      res.append(s)

    print(DE.join(res))
    return DE.join(res)
    

  def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    res = []
    chunks  = s.split(DE)
    for chunk in chunks:
      chunk = chunk.replace(ENCODE, ORI)
      res.append(chunk)
    
    print(res)
    return res

code = Codec()
encoded = code.encode(['aaa', 'bbb', 'c###', 'c#1#'])
code.decode(encoded)