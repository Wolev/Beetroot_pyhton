class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old.")


dude_1 = Person('Adrian', 'Paun', 25)
dude_1.talk()
