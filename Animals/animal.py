class Animal:

    # Animal initialization
    def __init__(self, name, species, gender, age):
        self.animal_name = name
        self.animal_species = species
        self.animal_gender = gender
        self.animal_age = age

    # Setters
    def change_animal_name(self, new_animal_name):
        self.animal_name = new_animal_name

    def change_animal_age(self, new_animal_age):
        self.animal_age = new_animal_age

    # Getters
    def get_animal_name(self):
        return self.animal_name

    def get_animal_age(self):
        return self.animal_age

    def get_animal_species(self):
        return self.animal_species

    def get_animal_gender(self):
        return self.animal_gender

    # Prints the animal's information
    def print_animal_info(self):
        print("Name: ", self.animal_name)
        print("Species: ", self.animal_species)
        print("Gender: ", self.animal_gender)
        print("Age: ", self.animal_age)
