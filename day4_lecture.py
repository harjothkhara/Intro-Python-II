class Animal:
    def __init__(self):
        self.name = 'Animal'
        self.sound = 'animal noise'


​
self.secret_number = 982
​


def __str__(self):
        return f"<Animal: {self.name}, {self.sound}>"


​


def make_sound(self):
        print(self.sound)


​


class Cat(Animal):
    def __init__(self):     # overriding the __init__ method
        super().__init__()
        self.name = "cat"
        self.sound = "meow"


​
​


class Dog(Animal):
    def __init__(self):     # overriding the __init__ method
        super().__init__()
        self.name = "dog"
        self.sound = "arf"


​
animals = [Cat(), Dog(), Dog(), Cat(), Cat(), Dog()]
​
for a in animals:
    a.make_sound()
