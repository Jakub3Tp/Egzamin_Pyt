import abc
class Animal:
    @abc.abstractmethod
    def say_hi(self):
        ...

class Dog(Animal):
    def say_hi(self):
        print("Woof")

class Cat(Animal):
    def say_hi(self):
        print("Meow")

if __name__ == "__main__":
    animal = [Dog(), Cat()]
    for animal in animal:
        animal.say_hi()