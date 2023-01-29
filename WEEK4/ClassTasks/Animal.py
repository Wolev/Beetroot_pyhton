class Animal:
    def __init__(self, name, colour, kind, number_of_legs):
        self.name, self.colour, self.kind, self.number_of_legs = name, colour, kind, number_of_legs

    def print_information(self):
        modifier = ''
        if self.name[0] in "aeiou":
            modifier = 'an'
        else:
            modifier = 'a'
        print(f"hi, I'm {modifier} {self.kind}, I have {self.number_of_legs} legs and my color is {self.colour}. My name is {self.name}.")

    def __str__(self):
        modifier = ''
        if self.name[0] in "aeiou":
            modifier = 'an'
        else:
            modifier = 'a'
        return f"hi, I'm {modifier} {self.kind}, I have {self.number_of_legs} legs and my color is {self.colour}. My name is {self.name}."

puma = Animal("Puma", "black", "feline", "four")
hawk = Animal("Hawk", 'greyish', 'bird', "two")

puma.print_information()
hawk.print_information()
print("\n")
print(puma)
print(hawk)

