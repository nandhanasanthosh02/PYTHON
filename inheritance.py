# INHERITANCE

# 1. Single inheritance
# 2. multi-level inheritance
# 3. multiple inheritance





# class Person1():  SINGLE LEVEL INHERITANCE
#     def __init__(self):
#         pass

#     def run(self):
#         print('person is running')

#     def walk(self):
#         print('person is walking')

#     def wite(self):
#         print('person is writing')
# class Person2():
#     def __init__(self):
#         pass
        
#     def eat(self):
#         print('person is eating')
    
#     def sleep(self):
#         print('person is sleeping')

# p2 = Person2()
# p2.sleep()


# class Person1():
#     def __init__(self):
#         pass

#     def run(self):
#         print('person is running')

#     def walk(self):
#         print('person is walking')

#     def write(self):
#         print('person is writing')

# class Person2(Person1):#--------> INHERITANCE
#     def __init__(self):
#         pass
        
#     def eat(self):
#         print('person is eating')
    
#     def sleep(self):
#         print('person is sleeping')

# p2 = Person2()
# p2.sleep()
# p2.write()   #-------->p2 can inherit the properties of p1



# class Person1():
#     def __init__(self):
#         pass

#     def run(self):
#         print('person is running')

#     def walk(self):
#         print('person is walking')

#     def write(self):
#         print('person is writing')

# class Person2(Person1):#--------> INHERITANCE
#     def __init__(self):
#         pass
        
#     def eat(self):
#         print('person is eating')
    
#     def sleep(self):
#         print('person is sleeping')
    
# class Person3(Person2):
#     def fly():
#         print('Person is flying')

#     def laugh():
#         print('Peron is laughing')

    
#     def sleep(self):
#         super().sleep()
#         print('person is sleeping')
    

# p3 = Person3()#-------Multilevel inheritance
# p3.sleep()
# p3.write()   #-------->p2 can inherit the properties of p1


# class Person1():
#     def __init__(self):
#         pass

#     def run(self):
#         print('person is running')

#     def walk(self):
#         print('person is walking')

#     def write(self):
#         print('person is writing')

# class Person2():#--------> INHERITANCE
#     def __init__(self):
#         pass
        
#     def eat(self):
#         print('person is eating')
    
#     def sleep(self):
#         print('person is sleeping')
    
# class Person3():

#     def __init__(self):
#         pass

#     def fly():
#         print('Person is flying')

#     def laugh():
#         print('Peron is laughing')

    
#     def sleep(self):
#         # super().sleep()
#         print('person is sleeping')

# class Person4(Person3,Person2,Person1):#-------Multiple inheritance
    
#     def cry():
#         print('person is crying')
        
    
    

# p4 = Person4()
# p4.sleep()
# p4.write()  