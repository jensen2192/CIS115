class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # def __str__(self):
       # return "Pet Name: " + self.__name + \
               # "\nAnimal Type: " + self.__animal_type + \
               # "\nPet Age: " + self.__age

def main():
    name = input("Enter the name of the pet: ")
    animal_type = input("Enter what type of animal the pet is: ")
    age = int(input("Enter the age of the pet in years: "))

    current_pet = Pet(name, animal_type, age)

    print("\nHere is the data that you entered:")
    print("Name:", current_pet.get_name())
    print("Animal type:", current_pet.get_animal_type())
    print("Age in years:", current_pet.get_age())

main()