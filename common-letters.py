# INTERVIEW QUESTION - Find out common letters between two strings Using Python

def common_letters():
    # ask for input
    str1 =input("please provide the 1st word: ")
    str2 =input("please provide the 2nd word: ")
    
    #convert the string into set to strip away any duplicates 
    s1 =set(str1)
    s2 =set(str2)
    
    # validation check (if required)
    # print(s1)
    # print(s2)
    
    # create a new list from items is s1 and s2 are the same 
    lst =s1 & s2
    print(lst)


# call the function 
common_letters()