from os import link
from unicodedata import decimal


def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number more than zero (limit 200)"
        text_error = "Please enter a whole number"
        
        try:
                
            # ask user for a number
            response = int(input(question))
            
            # checks number is more than 0
            if response in range(1, 200):
                return response
            
            #outputs error if input is invalid 
            else:
                print(error)
                print()
            
        except ValueError: 
            print(text_error)

to_factor = num_check("What number should I factorise? ")

