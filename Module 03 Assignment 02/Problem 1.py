""""
Inheritance and Advanced OOP Features

Create a base class Animal and a derived class Dog that inherits from Animal.

Output:

Animals make different sounds. # From Animal class

Dog barks! # From Dog Class

"""
class Animal:
    def speak(self):
        print("Animal make different sounds.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks!")


dog = Dog()
dog.speak()
