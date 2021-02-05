#YUCEL TASKIRAN
#Created 3 classes Animals,Dogs and cats...

class Animal:
    def __init__(self,name,specie_type):
        self.name=name
        self.specie_type=specie_type
    def printname(self):
        print("The name of animal is:",self.name)
    def printspecie(self):
        print("The type of specie is:",self.specie_type)
class Dog(Animal):
    def __init__(self, name, specie_type,pet_name):
        super().__init__(name, specie_type)
        self.pet_name=pet_name
    def printpetname(self):
        print("The pet name is:",self.pet_name)

dog= Dog("Dog","Golden","Bolt")
dog.printname()
dog.printspecie()
dog.printpetname()

class Cat(Animal):
    def __init__(self, name, specie_type,food, pet_name):
        super().__init__(name, specie_type)
        self.food=food
        self.pet_name=pet_name
    def printfood(self):
        print("The cat likes:", self.food)
    def printpetname(self):
        print("The pet name is:",self.pet_name)
cat= Cat("Cat","Van Kedisi","Mama","Silver")
cat.printname()
cat.printfood()
cat.printspecie()