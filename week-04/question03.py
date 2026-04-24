class Animal:
    def speak(self):
        print("Animal makes a Sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()