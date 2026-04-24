class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = Person("Sanajaya",23)
p2 = Person("Maaya",23)

p1.introduce()
p2.introduce()

