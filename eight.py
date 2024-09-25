# OK.  Let's start with algorithm...
# Can you see that this is an English-language version
# of the problem with a  bit more detail?

# Responses:
# All stored in a list called 'fortunes'
# Yes, no, likely, doubtful, positive, not going to happen, for sure, never

fortunes = ["Yes", "no", "likely", "doubtful"
            , "positive", "not going to happen", "for sure", "never"]

# Print a menu:
# All the fortunes
# Specific fortune
# Get a random

print("""
1. All the fortunes
2. Specific fortune
3. Get a random
""")

# Get string input -> userChoice
userChoice = input("What will you do? ")

# If userChoice is "1":
if userChoice == "1":
    #    Go through each fortune
    for index, value in enumerate(fortunes): 
        #    Print that fortune's index and value
        print(f"{index}) {value}")


# If userChoice is "2":
elif userChoice == "2":
    #    Ask for an index
    index = input("Which fortune do you want to see? (0-7) ")
    #    Check to see that index is a number *
    #        Check to see that index is in a legal range *
    #            Convert index to an integer
    index = int(index)
    #            Use that integer to print the corresponding fortune
    print(fortunes[index])

# 
# If userChoice is "3":
#   Ask the user for a question
#   Roll a random number suitable for the list (0 through n-1)
#    Print out the corresponding fortune
# 
# If userChoice is anything else:
#   Tell user they need to enter 1, 2, or 3
# 