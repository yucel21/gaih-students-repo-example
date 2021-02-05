#YUCEL TASKIRAN
#Company Management System : Employees, Manager

class Personel():
    
    def __init__(self,name, surname, city, ability, salary, position): 
        print("Created a new personel", name)
        self.name = name
        self.surname = surname
        self.city = city
        self.ability = ability
        self.salary = salary
        self.position = position
        self.language = []

    def addLanguage(self,new_lang):
        self.language.append(new_lang)
    
    def showInfo(self):
        print("*-"*20)
        print("NAME: ",self.name)
        print("SURNAME: ", self.surname)
        print("CITY: ",self.city)
        print("ABILITY: ",self.ability)
        print("SALARY: ",self.salary)
        print("POSITION: ",self.position)
        print(f"{self.name} can speak: ")
        for i in self.language:
              print(i)
        print("*-"*20)

class manager(Personel):

   
    def __init__(self,name, surname, city, ability, salary, position,managerAbility):
        super().__init__(name, surname, city, ability, salary, position)
       
        self.managerAbility = managerAbility
    def showInfo(self):
        super().showInfo()
        print("MANAGER ABILITY: ",self.managerAbility)
        print("*-"*20)
    


yucel = Personel("Yucel","Taskiran","Istanbul","C#,Python",3600,"Engineer")
asim = Personel("Asim","Direk","Istanbul","Network",3900,"Network")
mary = Personel("Mary","Joe","London","Linux,Java",3300,"Developer")
emel = manager("Emel","Neuer","Istanbul","UI and UX",6500,"Manager","Senior Software")
yucel.addLanguage("Turkish"),yucel.addLanguage("English"),
asim.addLanguage("English"),asim.addLanguage("Turkish")
mary.addLanguage("English"),mary.addLanguage("Turkish")
emel.addLanguage("Turkish"),emel.addLanguage("English"),emel.addLanguage("French"),emel.addLanguage("Spanish")


asim.showInfo()
yucel.showInfo()
mary.showInfo()
emel.showInfo()

