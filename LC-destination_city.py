# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
# Example 1 
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

# Example 2:

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: paths = [["A","Z"]]
# Output: "Z"

# create a dictionary that will count the cities  and look for a city that does not have any outgoing  routes from it (ie. it is not in position 0) of any of the nested arrays . This is our destination 
class Solution:
    def destCity (self, paths: list [list[str]]) -> str:
        # create an empty dict to keep a track of our results 
        outgoing_count = {}
        # loop over the paths in our array 
        for path in paths: 
            city_a , city_b = path #unpack each city from a nested array into a variable A / B
            # every city that is fond in the array gets added to the dict and counted . Count for City_a is incremented by 1 . City_b is added but with value 0 which we will be looking for in the next section of the solution 
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) +1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
            
        for city in outgoing_count:
            if outgoing_count[city] ==0 :
                return city
                
            
            
        


# checking the result 

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]  
paths2 = [["B","C"],["D","B"],["C","A"]]   
solution = Solution()
exercise = solution.destCity(paths)
exercise2 = solution.destCity(paths2)

print(exercise)
print(exercise2)