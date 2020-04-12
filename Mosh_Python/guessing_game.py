chance = 3
# get a myth number, and check : whether it is a number and whether it is in
# range (0-9)
myth = input("your myth number: ")
if myth.isdigit():
    myth = int(myth)
    if myth > 9 or myth < 0:
        print("please enter a number in range (0-9)")
        quit()
else:
    print("only numbers are allowed!")
    quit()

# guess game implemented below
print(f'This is a guessing game, and you have {chance} chances to guess the '
      f'mythical number (0-9)')
guess = 11
while chance > 0:
    guess = input("Guess: ")
# checking the input whether is a number and whether in range
    if guess.isdigit():
        guess = int(guess)
        if guess > 9 or guess < 0:
            print("please enter a number in range (0-9)")
        elif int(guess) == int(myth):
            print(f"You guess right! Good one! Only takes you {4-chance} "
                  f"times to guess")
            break
        else:
            print("Wrong guess! Try again!")
    else:
        print("only numbers are allowed!")

    chance -= 1
else:
    print("Sorry, you loose :(")
