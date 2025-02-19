n=int(input("Enter the no of oranges: "))

diameter=list(map(int,input().split()))

k=0 

for i in range(n):
    if (diameter[i]<=diameter[n-1]):
        diameter[i],diameter[k]=diameter[k],diameter[i]
        k+=1

print(diameter)