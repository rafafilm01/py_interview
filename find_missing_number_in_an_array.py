# FIND MISSING NUMBER IN AN ARRAY(SUMMATION & X-OR) - PYTHON INTERVIEW QUESTION
# using summation method  
example_array = [1,2,4,5,6,7]


lst=[1,3,5,6,7,8,20]
def missing_no(lst):
    # create an empty array (list) 
    list1=[]
    # loop over the range of items (with 1 being start and lst[-1] being the last item in the list) if a number is not preset , append it to list1 which is then returned 
    for i in range(1,lst[-1]):
        if i not in lst:
            list1.append(i)
    return (list1)

print(missing_no(example_array))
# solution using summation --> sum of natural numbers 

