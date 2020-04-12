print("This is a Car game simulation! Use 'help' to get the instructions")
user_command = ""
car_status = "stop"
while True:
    user_command = input("> ").lower()
    if car_status == user_command:
        print(f"Car is already {car_status}")
    else:
        if user_command == "help":
            print('''
            start   --  to start the car
            stop    --  to stop the car
            quit    --  to exit
            ''')
        elif user_command == "start":
            car_status = user_command
            print("Car is started ... Ready to go!")
        elif user_command == "stop":
            car_status = user_command
            print("Car stopped!")
        elif user_command == "quit":
            print("Game quit ... ")
            break
        else:
            print("I don't understand that ...")
