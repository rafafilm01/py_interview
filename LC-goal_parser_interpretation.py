# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:

# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:

# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"


class Solution:
    def interpret(self, command: str) -> str:
        # use string replacement method. NOTE it is possible to use more than 1 replace method at the same time
        return command.replace("()", "o").replace("(al)", "al")
    
my_string = "G()()()()(al)"

solution = Solution()
xercise =solution.interpret(my_string)
print(xercise)
       
        