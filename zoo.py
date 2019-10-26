from Animals.animal import *


class Zoo:
    # Zoo initialization
    def __init__(self):
        self.zoo_name = "The Zoo"
        self.zoo_capacity = 10
        self.zoo_count = 0
        self.list_of_animals = []

    # Renames the Zoo
    def change_zoo_name(self):
        print("Enter new name for zoo: ")
        new_name_for_zoo = input()
        self.zoo_name = new_name_for_zoo

    # Changes the capacity of the zoo
    def change_zoo_capacity(self):
        print("Enter the new capacity: ")
        new_capacity = int(input())
        if new_capacity < 0:
            print("Capacity cannot be less than zero.")
        elif new_capacity < self.zoo_count:
            print("Your capacity cannot be less than the current number of animals!")
        else:
            self.zoo_capacity = new_capacity

    # Adds an animal to the zoo if there is space
    def add_animal_to_zoo(self):
        if self.zoo_count < self.zoo_capacity:
            print("Enter the species: ")
            new_animal_species = input()
            print("Enter the name: ")
            new_animal_name = input()
            print("Enter the gender: (M/F) ")
            new_animal_gender = input()
            if new_animal_gender.lower() == "m":
                gender = "male"
            else:
                gender = "female"

            print("Enter the age:")
            new_animal_age = input()

            new_animal = Animal(new_animal_name, new_animal_species, gender, new_animal_age)

            self.list_of_animals.append(new_animal)
            self.zoo_count += 1
        else:
            print("Cannot add more animals to the zoo.")

    # Removes an animal from the zoo if it exists
    def remove_animal_from_zoo(self):
        print("Input the name of the desired animal.")
        animal_to_remove = input()
        for animal in self.list_of_animals:
            if animal_to_remove == animal.animal_name:
                self.list_of_animals.remove(animal)
        self.zoo_count -= 1

    # Prints the Zoo's information
    def print_zoo_info(self):
        print("")
        print("Zoo Information")
        print("Name: ", self.zoo_name)
        print("Capacity: ", self.zoo_capacity)
        print("List of Animals: ")
        for animal in self.list_of_animals:
            print("")
            animal.print_animal_info()
