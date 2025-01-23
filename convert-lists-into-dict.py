# INTERVIEW QUESTION - Conversion of two list into Dictionary Using Python . each item from lsit 1 corresponds with an item on list 2

def convert_lists_into_dict() : 
    key_list = [990, 9909, 2221, 1]
    value_list = ["raf", 'brian' , "steven", "john", "game"]
    
    # use zip method to combine 2 lists , one zip is done convert it into a dictionary 
    # NOTE any values / keys without a pair will be disregarded 
    result = dict(zip(key_list, value_list))
    
    print (result)
    
    
def convert_dict_into_tuples():
    
    sample_dict = {1: "one", 2: "two", 3: "three"}
    for i in sample_dict.items():
        print(i)
    


convert_lists_into_dict()
convert_dict_into_tuples()