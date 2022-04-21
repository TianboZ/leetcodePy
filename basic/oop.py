class Test1:
  num = 100 # class varialbe

  def __init__(self, a, b): 
    self.a = a # instance variable
    self.b = b

  
  def getAB(self): # regular method, bound with instance
    return self.a 

  def getCount(self):
    print(self.num)
    # self.getAB()
  
  @classmethod
  def iamclassmethod(cls, b): # class method
    cls.num = 101
    print(b)

  @staticmethod
  def iamstaticmethod(a):   # static method, bound with class
    print('static method', a)

t1 = Test1(1, 2)
# t2 = Test1()

#t1.name = 'tianbo'

# print(t1.a, t1.b)
# print(t2)
print(t1.num)
print(Test1.num)
# print(Test1.getAB()) # wrong!
print(t1.getAB())

print(Test1.iamstaticmethod('!'))
print(Test1.iamclassmethod('~'))

print(Test1.num)
print(t1.num)

