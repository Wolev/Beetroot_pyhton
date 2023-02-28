# Modify the recursive function in order to make it print "start" exactly 5 times

# you can put something here as well

def recursive_function(number):  # you can modify this line as well
    # you can put something here
    if number == 0:
        return
    print("start")  # but don't modify this one (no putting it inside a loop or whatever)
    recursive_function(number-1)  # you can modify this line instead
    # and put something here


recursive_function(5)