# Find minimum difference between two elements of Binary Tree
arr =[5, 32, 45, 12, 18, 25, 2]

def minimum_diff_ele (arr):
    #sort the array ascending , initialize the first difference value to be largest.
    sorted_arr = sorted(arr)
    size_of_arr = len(sorted_arr) # will be used in a FOR loop when setting the range 
    print(sorted_arr)
    min_diff = 9999*999 #creating the largest element which will be used to compare against 

    #  start comparing  the difference  of first elements with it 

    for i in range(0, size_of_arr -1):
        if(sorted_arr[i+1] -sorted_arr[i] < min_diff):
            min_diff = sorted_arr[i+1] -sorted_arr[i]
            # min_diff value will be overwritten each time a smaller value is provided 
        
            
        return min_diff
        
        
# call the function 
print(minimum_diff_ele(arr))