# POLYMORPHISM
# class Duck:
#     def __init__(self):
#          pass
#     def walk(self):
#          print('can walk')

#     def quack(self):
#         print('can quack')


# class Chick:
#      def __init__(self):
#          pass
     
#      def walk(self):
#         print('can walk')
    
#      def fly(self):
#          print('can fly')

# class farmer():
#     def __init__(self):
#          pass
     
#     def cook(self,bird):
#         bird.walk()
# d1=Duck()
# c1=Chick()

# class students:
#    def __init__(self,m1,m2):
#       self.m1=m1
#       self.m2=m2
    
#    def __add__(self,other):
      
#       t1=s1.m1+s1.m2
#       t2=s2.m1+s2.m2
#       return(t1,t2)
#    def __mul__(self,other):
#       t3=s1.m1*s1.m2
#       t4=s2.m1+s2.m2
#       return(t3,t4)
     
#    def __gt__(self,other)

# s1= students (7,9)
# s2= students (8,9)
# print (s1+s2)
# print (s1*s2)

# METHOD OVERLOADING AND OVERRIDING

# METHOD OVERLOADING

# Method overloading is not possible in pyhton since it is an interpreted languange
   
#METHOD OVERRIDING

# class A:
#     def __init__(self):
#         pass
#     def write(self):
#         print('writing')

# class B(A):
#     def __init__(self):
#         pass
#     def write(self):
#         print('b is writing') # Here the childclass override the parent class since the child class
# b=B()
# b.write()