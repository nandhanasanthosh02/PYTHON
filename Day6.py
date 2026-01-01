# program to find if there is vowel in the string or not
# data=input('enter a string:-')
# vowel='aeiow'
# for i in range(len(data)):
#     if data[i] in vowel:
#          print(f'{data[i]} in {[i]} ')
# data=input('enter a string:-')
# # vowel='aeiow'
# for i in range(len(data)):
#     if data[i] in 'aeiou':
#          print(f'{data[i]} in {[i]} ')

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         print('*',end='')
#     print()
# for i in range(1,6):
#     for k in range(6-i,0,-1):
#         print(' ',end='')
    
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# printing alphabets

# for i in range (1,6):
#     for j in range(1,6):
#         if j==1 or j==5 or i==3:
#             print('*',end=' ')
#         else:
#             print('',end='  ')

# #     print()
# for i in range (1,6):
#     for j in range(1,6):
#         if j==1 or j==5 or i==1 or i==3:
#             print('*',end=' ')
#         else:
#             print('',end='  ')

#     print()
# for i in range (1,6):
#     for j in range(1,6):
#         if j==1 or j==6 or i==1 or i==5:
#             print('*',end=' ')
#         else:
#             print('',end='  ')

# #     print()
# for i in range (1,6):
#     for j in range(1,6):
#         if j == 1 or (i == 1 and j < 5) or (i == 5 and j < 5) or (j == 5 and i != 1 and i != 5):
#             print('*',end=' ')
#         else:
#             print('',end='  ')

#     print()

#                        program to remove white space
# txt=input('Enter the sentence:-')
# wp=' '
# for i in txt:
#     if i!=' ':
#         wp=wp+i
#     else:
#         continue
# print(wp)


#           program to add words to a sentence

# count=int(input('Enter your count:'))
# sen=''
# for i in range (count):
#     word=input('enter your word:')
#     sen=sen+word+' '
# print(sen)