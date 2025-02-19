import quick_sort as qs

print("Enter the elements: ")
num=list(map(int, input().split()))

print(f"Original Array: {num}")

qs.quick_sort(num, 0, len(num)-1)

print(f"Quick Sorted Array: {num}")