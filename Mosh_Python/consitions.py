name = input("please enter your name: ")
if len(name) < 3:
    print("Your input is too short, name must be at least 3 characters")
elif len(name) > 51:
    print("Your input is too long, name must be maximum of 50 characters")
else:
    print(f"Welcome to the system, {name.title()}")
