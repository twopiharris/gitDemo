keepGoing = True
while keepGoing:
    print("I'm playing the game. It's fun")
    response = input("Do you want to play again? (Y/N)")
    response = response.upper()
    if response.startswith("Y"):
        keepGoing = True
    else:
        print("Thanks for playing...")
        keepGoing = False
        
