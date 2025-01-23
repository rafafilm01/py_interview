# Swap two variables
x= 5 
y= 10

print(f"x is set to {x}")
print(f"y is set to {y}")

# solution 1 --> using additional temp variable 
# temp = x 
# x = y
# y = temp


# solution 2 --> using tuple unpacking 

x, y = y, x



# validation block 
print (f"the value of x is : {x}")
print (f"the value of y is : {y}")