class MyNumber:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == getattr(other, 'value', other)

    def __gt__(self, other):
        return self.value >= getattr(other, 'value', other)

    def __lt__(self, other):
        return self.value <= getattr(other, 'value', other)

    def some_custom_method(self):
        print(self.value)

inst = MyNumber(23)
inst2 = MyNumber(25)

print(inst.__eq__(inst2))

# You can use inst.__dict__() to get the dictionary of values

# Polymorphism is when different types of objects have the same behaviour
