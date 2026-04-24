class Animal:
    def speak(self):
        print("Animal makes a Sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

dog = Dog()
dog.speak()