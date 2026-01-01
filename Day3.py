# CONTROL STATEMENTS

# 1 while
# 2 for

# while

# i=0
# while i < 10:
#     print(i)
#     i = i+1

# i=0
# sum=0
# while i <= 10:
#     print(i)
#     sum=sum+i
#     i = i+1
# print('sum =',sum)

# sum of first 100 even number
# i=0
# sum=0
# while(i<=100):
#     print(i)
#     sum=sum+i
#     i+=2
# print(sum)


# together

# i=0
# esum=0
# osum=0
# while(i<=100):
#     if i%2==0:
#         esum=esum+i
#     else:
#         osum=osum+i
#     i=i+1
# print(esum)
# print(osum)

# num=6
# i=1
# while(i<=10):
#     print(num,'X',i,'=',num*i)
#     i=i+1

# factorial
# num=5
# i=1
# fact=1
# while(i<=num):
#     print(i)
#     fact=fact*i
#     i=i+1
# print(fact)

# num=12345
# sum=0
# while(num>0):
#     i=num%10
#     sum=sum+i
#     num=num//10
# print(sum)

#reverse of number
num=43469
rev=0
while(num>0):
    i=num%10
    rev=rev*10+i
    num=num//10
print(rev)