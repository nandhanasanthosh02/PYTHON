# # print the sum of 2 X 2 matrix

# a=[[1,2],
#    [1,2]]
   
# b=[[1,2],
#    [1,2]]

# result=[[0,0],
#         [0,0]]


# for i in range(2):
#     for j in range(2):
#         result[i][j]=a[i][j]+b[i][j]
        
# for row in result:    
#    print(row)

# a=[[7,8],
#    [3,4]]

# b=[[1,2],
#    [4,5]]

# result=[[0,0],
#        [0,0]]

# for i in range(2):
#     for j in range(2):
#         result[i][j]=a[i][j]+b[i][j]

# for row in result:
#     print(row)


# programme to find the second lardest 

# numbers=[2,2,2]

# first=float('-inf')
# second=float('-inf')
# for num in numbers:
#     if num> first:
#         first=num
#     elif first > num > second:
#         second=num
        
# if second == float('-inf'):
#     print(None)

# else: print(second)

# p=["NANDHANA"]
# s=["NAMITHA"]
# pcount=0
# scount=0

# for i in range (len(p)-1):
#     if p[i]==p[i+1]:
#      pcount+=1
#     for char in (len(s)-1):
#      if s[i]==s[i+1]:
#       scount+=1
      
# print(pcount)

# word1 = "stop"
# word2 = "topss"

# # Convert words to lists of characters
# w1 = list(word1)
# w2 = list(word2)

# # Sort the lists using .sort()
# w1.sort()
# w2.sort()

# # Compare the sorted lists
# if w1 == w2:
#     print("Anagram")
# else:
#     print("Not an anagram")

n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,i+1): 

        print(j,end=' ')
    print()
 
for i in range(1,n+1):

    for j in range(i,n): 

        print(j,end=' ')
    print()
 
  
 