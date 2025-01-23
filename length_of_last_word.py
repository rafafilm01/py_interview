# interview question --> find out the length of the last word in a sentence 

my_string = "tiiiiits"

def len_of_last_word(sentence):
# capture the last word in the sentence 

    last_word = sentence.split()[-1]
    
    
    print(last_word)
    # calculate the number of letters in a word 
    num_of_letters = len(last_word)
    # provide the solution 

    print(num_of_letters)
    


len_of_last_word(my_string)