# fibonacci sequence is a sequence in which each number is the sum of the 2 preceding nums
# good exercise to explore recursion and iterative techniques in programming 

def print_fibonacci( num): 
    # assigning 2 variables at the same time 
    a,b =0, 1
    # check for edge cases 
    if num < 1 :
        print ("null")
    elif num ==1:
        print(a)
    elif num ==2 :
        print(a)
        print(b)
    
    # calculate the finboancci sequence 
    elif num >2 :
        print(a)
        print(b)
        # generate the next num in the series 
        for i in range (num -2):
            c = a+b
            # update a and b to prepare for next iteration, variable re-assignment  
            a, b = b, c 
            #print the next term in the series 
            print(c)
            

print_fibonacci(1)