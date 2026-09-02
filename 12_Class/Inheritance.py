class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")

class Puppy(Dog):
    def play(self):
        print(self.name,"is playful")

my_puppy = Puppy(name="Max", age="2")
print(my_puppy.name)
print(my_puppy.age)
my_puppy.bark()