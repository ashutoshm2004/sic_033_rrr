a=[9,7,7,3,6,2,4,2,4,8]
n=len(a)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)