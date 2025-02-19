#Find  the nth term of  the given series: 1,2,2,3,3,5,5,7,8,11,13,13......
#Position starts from 0
#APPROACH: divide and conquer split  the series in set of even position elements and odd ones.
#even pos elems: 1,2,3,5,8,13 (fibonacci)   
#odd pos elems: 2,3,5,7,11,13 (prime nos)

n=int(input("Enter the value of n: "))

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
    
def prime(num):
    
if(n%2 == 0):
    