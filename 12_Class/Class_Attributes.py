class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")

my_dog = Dog(name="Buddy", age=3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()