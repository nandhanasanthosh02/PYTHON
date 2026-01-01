# a=[1,2,3,1,2,3,4,5,6,7,8,9,3,4,5,6,7]
# dup=[]
# for i in a:
#     if i not in dup:
#         dup.append(i)
# print(dup)
    
# a=[11,12,13,14,15,16,17,18,19,20]
# mid=len(a)//2
# l1=[]
# l2=[]
# for i in range(len(a)):
#     if i<mid:
#         l1.append(a[i])
#     else:
#         l2.append(a[i])
# print(l1)
# print(l2)

# input=hello how are you
# all the words should be in list
# data='hello how are you'
# result=""
# z=[]
# for i in data:
#     if i!=' ':
#         result+=i
#     else:
#         z.append(result)
#         result=" "
# z.append(result)
# print(z)

#print largest and smallest number

# x=[12,-2,-200,1229,0,20]
# largest=0
# smallest=0
# for i in x:
#     if i>largest:
#      largest=i
#     if i<smallest:
#        smallest=i
# print(f"The largest number is",{largest})
# print(f"the smallest number is",{smallest})

# # print the numbers in ascending order

# x = [65, 13, 132, 55, 677, 908, 3565, 42, 4, 34]
# asc = []

# while x:
#     min_val = x[0]
#     for num in x:
#         if num < min_val:
#             min_val = num
#     asc.append(min_val)
#     x.remove(min_val)

# print(asc)

# CHESS BOARD

# for i in range (1,9):
#     for j in range(1,9):
#         if (i + j) % 2 == 0:
#             print('w',end=' ')
#         else:
#             print('B',end=' ')
#     print()