class GrandParent:
    some_attribute = 10

    def __init__(self, age=90):
        self.age = age

    def __str__(self):
        print("I'm being run")
        return "something"

    def __eq__(self, other):
        return True

    def something_else(self):
        print("It works")
        

    @classmethod
    def something_else_again(cls):
        print(cls.some_attribute)


grand_parent = GrandParent()
grand_parent2 = GrandParent(age=20)


# these two lines are equal
grand_parent.something_else()
GrandParent.something_else(grand_parent)