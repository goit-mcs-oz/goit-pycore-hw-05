# Завдання 4

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Contact doesn’t exist.'
        except ValueError:
            return 'Enter the argument for the command'
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact doesn’t exist."


@input_error
def show_phone(args, contacts):
    name,  = args
    return contacts[name]


@input_error
def show_all(contacts):
    contacts_str = ''
    for key, value in contacts.items():
        contacts_str += f"{key} {value}\n"
    return contacts_str.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Enter a command.")
        else:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
