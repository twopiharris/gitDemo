# knock knock

#here's the most basic version


response = input("Do you want to hear a joke?")
if response == "yes":
    print("Here's my joke...")
else:
    print("It was going to be funny. Goodbye.")
        
# if you want to fix for upper / lowercase, you can change the condition
response = input("Do you want to hear a joke?")
response = response.upper()
if response == "YES":
    print("Here's my joke...")
else:
    print("It was going to be funny. Goodbye.")

# and you can check for 'starts with y' with this code:
response = input("Do you want to hear a joke?")
response = response.upper()
if response.startswith("Y"):
    print("Here's my joke...")
else:
    print("It was going to be funny. Goodbye.")

