def counttozero(n):
    print(n)
    if n==0:
        return 0
    else:
        return counttozero(n-1 )
a=10
counttozero(a)