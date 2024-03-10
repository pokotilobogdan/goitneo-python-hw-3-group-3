from commands import *
from colorama import Fore


def main():  # maybe add 'help' command
    book = AddressBook()
    print(Fore.CYAN + "Welcome to the assistant bot!")

    while True:
        user_input = input(Fore.CYAN + "Enter a command: " + Fore.RESET)
        if user_input == '':
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print(Fore.CYAN + "Good bye!" + Fore.RESET)
            break
        elif command == "hello":
            print(Fore.CYAN + "How can I help you?")
        elif command == "help":
            pass
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_contact(args, book))
        elif command == "all":
            print(show_all_contacts(book), end='')
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "birthdays":
            birthdays(book)
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
