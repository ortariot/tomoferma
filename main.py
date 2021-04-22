# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

# гусей "Серый" и "Белый"
# кур "Ко-Ко" и "Кукареку"
# и утку "Кряква"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# коз "Рога" и "Копыта"

# Со всеми животными вам необходимо как-то взаимодействовать:

# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)

# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить 
# общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.

from random import randint

class Animal():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def eat(self, food):
        print(f"I'am {self.name}, I'am eat {food}")
    
    def say(self):
        print(f"I'm {self.name}, I say {self.voice[self.kind]} ")

    voice = {"gose" : "Ga-ga-ga", 
            "chicken" : "Ko-ko-ko", 
            "duck" : "Krja-Krja", 
            "cow" : "Muuuuu", 
            "sheep" : "Be-be-be", 
            "goat" : "Me-me-me" 
            }

class Bird(Animal):
    def get_edge(self):
        return randint(0,4)

class Milk_Giving(Animal):
    def get_milk(self):
        return randint(0, 15) if self.kind is "cow" else randint(0, 8)

class Wool_Giving(Animal):
    def get_wool(self):
        return randint(0, 3)



def main():
    dog = Animal("Druzok", "dog")
    dog.eat("meat")
    ko_ko = Bird("Ko-Ko", "chicken")
    print(f"{ko_ko.name} lsid {ko_ko.get_edge()} edges")
    ko_ko.say()
    mu_mu = Milk_Giving("Mu-mu", "cow")
    print(f"{mu_mu.name} lsid {mu_mu.get_milk()} litrs milk")
    kozlina = Milk_Giving("Kozlina", "goat")
    print(f"{kozlina.name} lsid {kozlina.get_milk()} litrs milk")

main()
