#object oriented programming 
# Object-------> real wworld entitnty
           
#            1. Attributes---->deifnes a object

#            2. Behavior------->what an object can do/ functions of object

# Class------------->Blueprint used to create object



# class Car:
#     def start():
#         print('car has started')
#     def stop():
#         print('Car has stopped')
# car1=Car
# car1.start()
# car1.stop()

# car2=Car
# car2.start()
# car2.stop()


# PEP-----Python Enhanced Proposal-8----documentation of following standard and clean way to write python program

#CONSTUCTOR ---->IS A METHOD TOINITIALIZE OBJECT (__INT__)--->MAGIC METHOD

# class Car:
#     def __init__(self): #self points to car1
#         # print('the car has created')
#         self.color='Red'
#         self.brand='Porsche'

#     def start(self):
#         print('car has started')
#     def stop(self):
#         print('Car has stopped')

# car1=Car()
# print(car1.color)
# print(car1.brand)
# car1.start()
# car1.stop()

# car2=Car
# car2.start()
# car2.stop()

# class Car:
#     def __init__(self,col,brd): #self points to car1
#         # print('the car has created')
#         self.color=col
#         self.brand=brd

#     def start(self):
#         print('car has started')
#     def stop(self):
#         print('Car has stopped')

# car1=Car('Blac','Lamborgini')
# car2=Car('green','Ferrari')
# print(car1.brand)
# print(car2.color)
# # print(car1.brand)
# # car1.start()
# # car1.stop()

class students():
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name= name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5

    def total_mark(self):
        return self.m1+self.m2+self.m3+self.m4+self.m5
    
    def average(self):
        return self.total_mark()/5

s1=students('namitha',90,99,97,95,96)
print(s1.total_mark())
print(s1.average())
