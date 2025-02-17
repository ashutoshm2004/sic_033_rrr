import math
num=int(input("Enter a positive number:"))
num_root=int(math.sqrt(num))
if(num_root*num_root == num):
    print("Perfect Square")
else:
    print("Not Perfect Square")