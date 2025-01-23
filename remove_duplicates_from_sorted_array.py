# Remove Duplicates from Sorted Array

list_with_dups = [1,1,2,3,4,5,5,6,7,8,9]

## solution 1 . convert to a set variable type 

new_set = set(list_with_dups)
print(list(new_set))


## solution 2 use a for loop - less efficient solution 
new_list = []
for i in list_with_dups:
    if i not in new_list:
        new_list.append(i)
print(new_list)