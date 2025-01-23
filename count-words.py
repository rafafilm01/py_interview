# INTERVIEW QUESTION - Count the frequency of words appearing in a string Using Python
# eg of 2 sentences : 
# s1 = "sheena loves eating apple and mango . Her sister also loves eating apple and mango"

# return the sentences in a form a dictionary where they key is the word and the value is the count of the word

def freq_words (): 
    str = input("Enter a sentence: ")
    # convert the string into a list 
    list_of_words = str.split()
    # create an empty dictionary that will be populated by the values form list_of_words 
    dict = {}
    
    # loop over all words in the list_of_words and assign them as keys 
    for i in list_of_words:
        if i not in dict.keys(): # condition to see if a word is already in the dict
            # if the word is not yet in the dict add it with value set to 0
            dict[i] =0
        # if the word already exist (or just had been added above), increment the count by 1 
        dict[i] = dict[i] +1
    # once the loop completes , print the dictionary 
    print(dict)
    



#### ALTERANTIVE SOLUTION USING GET METHOD 

def freq_words2 ():
    str = input("Enter a sentence: ")
    # convert the string into a list 
    list_of_words = str.split()
    # create an empty dictionary that will be populated by the values form list_of_words 
    dict = {}
    
    for i in list_of_words:
        dict[i] = dict.get(i,0) +1
        
    print(dict)
    

# call the function 
# freq_words()
freq_words2()