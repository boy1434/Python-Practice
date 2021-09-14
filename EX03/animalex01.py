
class Animal:
    def sound(self):
        print("동물소리")


class Dog(Animal):
    def sound(self):
        print("강아지 소리")


d = Dog()
d.sound()

a = Animal()
a.sound()
