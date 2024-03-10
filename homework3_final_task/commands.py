from CLI import Phone
from CLI import Birthday
from CLI import Record
from CLI import AddressBook
from colorama import Fore
from decorators import *


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list[str], book: AddressBook):  # works well (add ability to write down more than one number ???)
    name_str, phone_str = args

    for name in book.keys():
        if name.value == name_str:
            return book[name].add_phone(phone_str)

    new_phone = Phone(phone_str)
    if new_phone.is_valid():
        new_contact = Record(name_str)
        new_contact.add_phone(phone_str)
        book.add_record(new_contact)
        return Fore.GREEN + "Contact is added."
    # else:
    #     return Fore.RED + f"The phone number {phone_str}" + Fore.RED + " is not valid." + Fore.RESET


@change_error
def change_contact(args: list[str], book: AddressBook):  # works well
    name_str, old_phone_str, new_phone_str = args

    contact = book.find(name_str)
    if contact.find_phone(old_phone_str) is True:
        return contact.edit_phone(old_phone_str, new_phone_str)
    else:
        return Fore.RED + "There is no such number to edit. Maybe you wanna add new number?"


@show_error
def show_contact(args: list[str], book: AddressBook):  # works well
    name_str = args[0]
    for name in book.keys():
        if name.value == name_str:
            return str(f"{name}: {'; '.join(p.value for p in book[name].phones)}")
    else:
        return Fore.RED + "Contact is not found"


def show_all_contacts(book: AddressBook):  # works well
    users = ''
    for name in book.keys():
        users += str(book[name]) + '\n'
    return users


@birthday_error
def add_birthday(args: list[str], book: AddressBook):  # works well
    name_str, birthday_str = args
    birthday = Birthday(birthday_str)
    if birthday.isvalid():
        for name in book.keys():
            if name.value == name_str:
                return book[name].add_birthday(birthday)


@birthday_error
def change_birthday(args, book):  # works well
    name_str, birthday_str = args
    birthday = Birthday(birthday_str)
    if birthday.isvalid():
        contact = book.find(name_str)
        contact.birthday = birthday
        return Fore.GREEN + "Birthday field is changed"
    else:
        return Fore.GREEN + "Something is wrong. Nothing has changed."


@show_error
def show_birthday(args: list[str], book: AddressBook):  # works well
    name_str = args[0]
    for name in book.keys():
        if name.value == name_str:
            return book[name].birthday


def birthdays(book: AddressBook):  # works well
    return book.get_birthdays_per_week()
