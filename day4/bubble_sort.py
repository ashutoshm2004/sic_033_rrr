# a=[9,7,7,3,6,2,4,2,4,8]
# n=len(a)
# for i in range(0,n-1):
#     for j in range(0,n-1-i):
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print(a)

def bubble_sort(array):
    for i in range (len(array)-1):
        for j in range (len(array)-i-1):
            if array[j]  > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def optimized_bubble_sort(array):
    for i in range (len(array)-1):
        sorted = True
        for j in range (len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                sorted = False
        if sorted:
            return
        
print('Enter the input numbers: ')
numbers = [int(num) for num in input().split()]

bubble_sort(numbers)
print('Sorted Array: ',numbers)
optimized_bubble_sort(numbers)
print('Optimized Sorted Array: ', numbers)