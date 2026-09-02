a = [1, 5, 8, 9, 4]
b = [2, 9, 30, 85, 33, 99]
c = a
d = [1, 5, 8, 9, 4]
print("a is b ",a is b)
print("a is d ",a is d) #not same memory location
print("a is c ",a is c) #true because same memoey location
print("a is not b ", a is not b)