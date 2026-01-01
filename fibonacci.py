# program to find Fibanocci series

n=int(input('Enter the number of terms:-'))

i=0
j=1
count=0
if n == 1:
    print('fibonacci series')
    print(i)

else:
    print('fibonacci series')

    while count<n:
        print(i)
    
        k=i+j
        i=j
        j=k
        count=count+1


    