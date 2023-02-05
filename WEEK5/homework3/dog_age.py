class Dog:

    def __init__(self, age):
        self.age = age
        self.age_factor = 7

    def human_age(self):
        human_age = self.age * self.age_factor
        print(f"The human age of this dog is {human_age} years old.")


dog_1 = Dog(2)
dog_1.human_age()

