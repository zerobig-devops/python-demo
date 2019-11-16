class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_Hello(self, to_name):
        print("Hi " + to_name + " I'm " + self.name)

    def introduce(self):
        print("My name is " + self.name + " and I'm " + str(self.age) + " years old")

class Police(Person):
    def arrest(serf, to_arrest):
        print("You are arrested, " + to_arrest)

class Programmer(Person):
    def program(serf, to_program):
        print("I will make this: " + to_program)

zero = Person("zero", 20)
big = Police("big", 21)
zerobig = Programmer("zerobig", 22)

big.introduce()
big.arrest("big")
zerobig.introduce()
zerobig.program("Email Client")
