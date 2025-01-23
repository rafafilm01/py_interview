# find_out_pair_with_given_sum_value_of_array
arr = [5, 7, 4, 3, 9, 8, 19, 21]
target_sum = 17

def find_pairs(arr, target_sum):
    # Create an empty hash set to store numbers we've seen
    seen = set()
    pairs = []
    
    for num in arr:
        # For each number, check if its complement (target_sum - num) exists in the set
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        # Add the current number to the set
        seen.add(num)
    print(f"here is the list of seen numbers : {seen}")
    print (f"here is the list of pairs that was discovered {pairs}")
    return pairs

# Find and print all pairs
result = find_pairs(arr, target_sum)
if result:
    print(f"Pairs with sum {target_sum}:")
    for pair in result:
        print(f"{pair[0]} + {pair[1]} = {target_sum}")
else:
    print(f"No pairs found with sum {target_sum}")
    
    