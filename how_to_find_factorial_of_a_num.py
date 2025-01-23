# factorial is a function that multiplies a number by every number below it till 1 
# factorial of 3 is 3 * 2 * 1 == 6


# solution 1 
def compute_factorial(num):
    # set factorial to starting position of 1 
    factorial =1
    # check if the num is applicable
    if num < 0: 
        print(" Sorry but factorial does not exist in negative numbers")
    # check for 0
    elif num ==0:
        print ("The factorial of 0 is 1 ")
        
    else:
        # the range is based on the number (so if the number is 4 the range will be 1 2 ,3 and 4 inclusively ) and will be used for multiplying 
        for i in range (1, num +1):
            factorial = factorial * i
        print(f"The factorial of {num} is {factorial}")
        
# solution 2 --> use existing values that get stored in memory dict
memory = {}
def factorial_memory(num):
    if num == 0:
        return 1
    if num in memory:
        return memory[num]
    memory[num] = num * factorial_memory(num - 1)
    return memory[num]
    


        
# call the function
compute_factorial(4)
factorial_memory(5)
print(f"here is the entire memory bank that has been created by FACTORIAL MEMORY so far: \n {memory}")
# NOTE each item the program is run memory will be wiped clean as it is set to be an empty dict. In order for this to work the code needs to be wither run in jupyter notes where values are stored or saved to a separate file. 