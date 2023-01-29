class EmptyClass():
    pass

def class_function(class_some):
    some_variable = class_some()
    return some_variable

print(class_function(EmptyClass))