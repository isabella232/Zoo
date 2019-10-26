from zoo import *

zoo = Zoo()

# Continuous loop to display information
while True:

    print("Check Zoo Information (i)")
    print("Add Animal (a)")
    print("Remove Animal (r)")
    print("Change Zoo Capacity (c)")
    print("Change Zoo Name (n)")
    print("Exit (x)")

    user_input = input()

    # Checks the users input and performs and action
    if user_input == 'x':
        break
    elif user_input == 'i':
        zoo.print_zoo_info()
    elif user_input == 'a':
        zoo.add_animal_to_zoo()
    elif user_input == 'r':
        zoo.remove_animal_from_zoo()
    elif user_input == 'c':
        zoo.change_zoo_capacity()
    elif user_input == 'n':
        zoo.change_zoo_name()
    else:
        print("Invalid Input")
