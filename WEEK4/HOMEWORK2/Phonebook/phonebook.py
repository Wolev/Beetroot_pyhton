import json


phonebook = {
    "+380972915744": {
        "first_name": "Roman",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "56789087678909": {
        "first_name": "Adrian",
        "second_name": "ABC",
        "city": "Queens",
        "state": "New York",
    },
    "67876764543": {
        "first_name": "Serap",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "65676545434": {
        "first_name": "Linus",
        "second_name": "ABC",
        "city": "Washington DC",
        "state": "Columbia"
    },
    "878007678755588": {
        "first_name": "Olena",
        "second_name": "Petrus",
        "city": "Washington DC",
        "state": "Columbia",
    },
}


def ask_user_info(answers=("first_name", "second_name", "city", "state")):
    return {
        answer: input(f"Write {answer} here please: ")
        for answer in answers
    }


def add(phone_number):
    phonebook[phone_number] = ask_user_info()


def update(phone_number):
    phonebook[phone_number].update(ask_user_info())


def delete(phone_number):
    del phonebook[phone_number]

def nothing():
    pass


def search_full_name(first_name, second_name):
    for phone_number in phonebook:
        if phonebook[phone_number]["first_name"] == first_name:
            if phonebook[phone_number]["second_name"] == second_name:
                print(f"Found {first_name} {second_name} with the phone phone_number: {phone_number}.")
                print(f"Phonebook entry: \n {phonebook[phone_number]}\n")
            else:
                print(f"{first_name} {second_name} not found in the phonebook.")
    else:
        print(f"{first_name} not found in phonebook.")


actions = {
    0: nothing,
    1: delete,
    2: add,
    3: update,
    4: search_full_name,
}

actions_to_print = {key: action.__name__ for key, action in actions.items()}
print("Available actions are:")
print(json.dumps(actions_to_print, indent=4))
action = input("Please say what you want to do: ")


if action == "4" or action == "0":
    pass
else:
    phone_number = input("Please type the phone_number: ")


if int(action) in range(1,4):
    actions[int(action)](phone_number)
elif int(action) == 0:
    actions[int(action)]()
else:
    first_name = input("Input the first name: ")
    second_name = input("Input the second name: ")
    actions[int(action)](first_name, second_name)


with open("phonebook.txt", "w+") as file:
    json.dump(phonebook, file)
    file.seek(0)

    new_phonebook = json.load(file)
    print("Full phonebook: ")
    print(new_phonebook)