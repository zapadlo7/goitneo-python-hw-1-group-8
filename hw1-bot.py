def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=1)
    cmd = cmd.strip().lower()
    return cmd, args[0].split() if args else []

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' added successfully."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments. Usage: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for contact '{name}'."
    else:
        return f"Contact '{name}' not found."

def get_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"Phone number for contact '{name}' is {contacts[name]}."
    else:
        return f"Contact '{name}' not found."

def get_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
