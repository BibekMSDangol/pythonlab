'''
car game:
        >help
        start - to start the car
        stop - to stop the car
        quit - to exit
        > asd
        I dont understand this
        > start
        ccar started... Ready to go!!
        > stop
        car stopped
        > quit
'''
command_repeat = 0
first_command = 'start'
second_command = 'stop'
third_command = 'exit'
while command_repeat<=2:
    command_repeat+=1
    user_command = input("Enter any command:")


    if user_command == first_command:
        print("Car staterd... Ready to go!!")
    elif user_command == second_command:
        print("Car stopped")
    elif user_command == third_command:
        print("Quit")
    else:
        print("I dont understand")

