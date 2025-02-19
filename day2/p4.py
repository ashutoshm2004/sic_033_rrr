def my_range(end: int, start=0, step=1):
    ll = []
    while start < end:
        start += step
        ll.append(start)
    
    return ll

print(my_range(10))
print(my_range(20, 10))
print(my_range(10, 20, 2))
print(my_range(20, 10, -2))