# check for natural numbers divisible by 1 or themselves (0 and 1 cannot be prime numbers and need to be excluded from the check) 

def check_prime(num):
    # Handle numbers that cannot be prime (negative numbers, 0, and 1)
    if num < 2:
        return False
    
    # Check divisibility from 2 to square root of number
    # We only need to check up to square root because if n=a×b, 
    # one of a or b must be ≤ √n
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If number is divisible by any i, it's not prime
            return False
    
    return True  # If no divisors found, number is prime

# Test the function with some examples
def main():
    test_numbers = [0, 1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    
    for num in test_numbers:
        if check_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")



# call the function 
print(check_prime(9))
main()
