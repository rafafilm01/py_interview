
### Exercise 1: Sum of Diagonals

# Create a function that returns the sum of both diagonals in a square matrix

Example =     [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
def sum_diagonals(matrix):
    n = len(matrix) 
    
    # calculate the main diagonal (top left to bottom right )
    sum_main = sum(matrix[i][i] for i in range(n))
    # When i = 0: matrix[0][0] -> gets top-left element
    # When i = 1: matrix[1][1] -> gets center element
    # When i = 2: matrix[2][2] -> gets bottom-right element
    

    # calculate the second diagonal (top right to bottom left )
    sum_secondary = sum(matrix[i][n-1-i] for i in range(n))
    # When i = 0: matrix[0][2] -> gets top-right element
    # When i = 1: matrix[1][1] -> gets center element
    # When i = 2: matrix[2][0] -> gets bottom-left element
    
    return (f" the value of first diagonal is : {sum_main} and the second diagonal is : {sum_secondary}. The sum is : {sum_main + sum_secondary}")
    

# print(sum_diagonals(Example))
    
#######################################
# Create a function that prints all border elements of a matrix

Example_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
 ]
def print_border(matrix):
    # if not matrix: return # check to see if value has been provided , otherwise return None --> does not work as expected
    rows , cols = len(matrix) , len(matrix[0])
    
    # print the top border - first row 
    for j in range(cols):
        print(matrix[0][j] , end=' ')  # use end modulator to present the results on a single line 
        
        
    # print the last column (right border, excluding the first element) 
    for i in range(1, rows):
        print ( matrix[i][cols-1] , end =' ')
    
    # check to see if there is more than 1 row
    if rows > 1 :
        for i in range (cols-2,-1,-1):
            print(matrix[rows-1][i], end=' ')
            
        # step 4 print first column in reverse (lef border , excluding first and last elements)
        for i in range(rows-2, 0, -1):
            print (matrix[i][0], end=' ')
                
    # return f"the table has {rows} rows and {cols} columns "
    
    # Should print: 1 2 3 4 8 12 11 10 9 5
    
print(print_border(Example_2))