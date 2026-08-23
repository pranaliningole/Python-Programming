a = "31.5"  # this is a string because it is written in double code 
t = type(a)
print(t)
print("\n")

a = "35.4"
t = float(a) # legal conversion from string to float
print(type(t))
print("\n")

a = "31.5"
t = int(float(a)) # string->float->int (legal coversion)
print(type(t))
print("\n")

a = "Pranali"
t = float(a) # illegal conversion from string ("Pranali") to float
