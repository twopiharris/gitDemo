#knock.py

userName = input("Hi, what is your name? ")
hearJoke = input(f"Do you want to hear a joke, {userName}? ")
hearJoke = hearJoke.upper()
if hearJoke.startswith("Y"):
    response = input("Knock Knock ")
    if response.upper() == "WHO'S THERE?":
        response2 = input("Boo ")
        if response2.upper() == "BOO WHO?":
            print("Don't cry.")
        else:
            print ("You were supposed to say 'boo who?'")
    else:
        print("You were supposed to say 'who's there?'")
else:
    print("It was going to be really funny.")
