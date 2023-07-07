
class Doodad:
    def __init__(self, name, age, DOB, sex):
        self.name = name
        self.age = age
        self.date_of_birth = DOB
        self.sex = sex
        
person1 = Doodad("lincoln", "18", "jan 29", "male")

print(person1.name)