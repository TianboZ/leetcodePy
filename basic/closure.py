def func(a, b):
  def func2(a = 1):
    print(a)
    print(b)
  
  func2()
func(100, 2)