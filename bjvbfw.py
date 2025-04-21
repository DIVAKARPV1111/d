class Parrot:

# instance attributes
 def __init__(self, name, age):
   self.name = name
   self.age = age

# instance method
 def sing(self, song):
   return '{} sings {}'.format(self.name, song)

 def dance(self):
   return '{} is now dancing'.format(self.name)

# instantiate the object
blu = Parrot('Blu', 10)
# call our instance methods
print(blu.sing('Happy'))
print(blu.dance())

for x in range(2, 6):
 print(x)

 
  class Parrot:
  
   def fly(self):
     print('Parrot can fly')
  
   def swim(self):
     print('Parrot can not swim')
  
  class Penguin:
  
   def fly(self):
     print('Penguin can not fly')
  
   def swim(self):
     print('Penguin can swim')
  
  # common interface
  def flying_test(bird):
    bird.fly()
  
  #instantiate objects
  blu = Parrot()
  peggy = Penguin()
  
  # passing the object
  flying_test(blu)
  flying_test(peggy)loop([timeout[,)
                
Function
def name(args):
 pass                Function
 def name(args):
  pass