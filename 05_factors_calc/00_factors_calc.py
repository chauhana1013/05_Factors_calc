# Functions go here
import math
import random
# Puts series of symbols at start and end of text
from turtle import heading


def  statement_generator(text, decoration):

    # Make string with 5 characters 
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculation as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""


# Checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number more than zero (limit 200)"
        text_error = "Please enter a whole number"
        
        try:
                
            # ask user for a number
            response = int(input(question))
            
            # checks number is more than 0
            if response <= 200:
                return response
            
            #outputs error if input is invalid 
            else:
                print(error)
                print()
            
        except ValueError: 
            print(text_error)


# Gets factors, returns a sorted list
def get_factors(to_factor):
    if to_factor == 1:
        return [1]
    
    # Use Math for calculations

    my_list = []
    num_sqrt = math.ceil(math.sqrt(to_factor))
    
    # +1 expanding range
    for num in range(1, num_sqrt + 1):
        if to_factor % num == 0:

            # find factor by division, get whole number only
            a_factor = to_factor // num

            my_list.append(a_factor)

            if num not in my_list:
                my_list.append(num)
    
    my_list.sort()
    
    # Unique factor stored
    return my_list


# Main Routine

# Heading
statement_generator("Factors Calculator", "-")

# Displays instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")
 
if first_time == "":
    instructions()

# Loop to allow multiple calculations per seesion
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factorised 
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comments

    # Generate heading
    if var_to_factor == 1:
        heading = "One is speacial"
    
    else: 
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comments
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using factors calculator, you're welcome for the help! ")
print()

#******Credits********
#thanks to Saahil, Zane and Ms G for helping me out
#P.S. Jayden was annoying JK