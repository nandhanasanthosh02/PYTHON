# file1=open('Tuesday.txt')
# print(file1.read())



# file1.close()
# file2=open('hai.txt','w')
# # file2.write('hello goodmorning')
# file2.write('get up its 6 am')
# file2.close()
# file3=open('hai.txt','a')
# file3.write('\nhello')
# file3.close()
# a= r"C:\\Users\\NANDHANA\\Desktop\\filee.txt"
# # file11=open(a)
# # print(file11.read())
# # file11.close()
# with open(a,'r') as f:
#     print(f.read()) #instead of uisng 3 4 lines cod ewe can just use this 2 lines direcclty.we dont want to close this file ,it will be auotmatically  closed

#     #CREATING ,DELETING AND UPDATING FOLDER

# import os

# os.mkdir('Nandhana')

# try:
#     a=5
#     b=-0
#     print(a/b)
# except:
#     print('error occured')
# print(a)

class MyError(Exception):
    pass

a=1
if a==1:
    raise MyError('a should not be 1')