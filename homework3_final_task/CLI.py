from collections import UserDict
from get_birthdays import get_birthdays_per_week
from datetime import date
from datetime import datetime
from colorama import Fore


class Field:
    def __init__(self, value: str):
        self.value = value
        self.optional = False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.optional = True


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def is_valid(self) -> bool:
        if self.value.isdigit() and len(self.value) == 10:
            return True
        else:
            return False


class Birthday(Field):  # expected DD.MM.YYYY
    def __init__(self, value):
        super().__init__(value)
        self.optional = True

    def __str__(self):
        day, month, year = self.value.split('.')
        months = {"January": ["1", "01"],
                  "February": ["2", "02"],
                  "March": ["3", "03"],
                  "April": ["4", "04"],
                  "May": ["5", "05"],
                  "June": ["6", "06"],
                  "July": ["7", "07"],
                  "August": ["8", "08"],
                  "September": ["9", "09"],
                  "October": ["10"],
                  "November": ["11"],
                  "December": ["12"]}
        for month_name, numbers in months.items():
            if month in numbers:
                return f"{day} {month_name} {year}"

    def isvalid(self) -> bool:
        try:
            day, month, year = self.value.split('.')
            _ = date(int(year), int(month), int(day))
            return True
        except ValueError:
            return False


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return Fore.YELLOW + f"Contact name: {self.name.value}\nbirthday: {self.birthday}\nphones: {'; '.join(p.value for p in self.phones)}\n"

    def __repr__(self):
        return str(self)

    def add_birthday(self, birthday: Birthday):
        if self.birthday is None:
            self.birthday = birthday
            return Fore.GREEN + f"Birthday is added"
        else:
            return Fore.RED + "Here is already birthday. Do you wanna change it?"

    def add_phone(self, new_phone_str: str):
        new_phone = Phone(new_phone_str)
        if new_phone.is_valid() is False:
            return Fore.RED + "The phone number " + \
                Fore.YELLOW + f"{new_phone}" + \
                Fore.RED + " is not valid."
        for phone in self.phones:
            if new_phone.value == phone.value:
                return Fore.RED + "There is already number " + \
                    Fore.YELLOW + f"{new_phone}" + \
                    Fore.RED + " in the record. Nothing is added."
        self.phones.append(new_phone)
        return Fore.GREEN + "Contact is added"

    def remove_phone(self, phone_to_remove: str):
        for phone in self.phones:
            if phone_to_remove == phone.value:
                self.phones.remove(phone)
                return None
        print(Fore.RED + "There is no number " + \
              Fore.YELLOW + f"{phone_to_remove}" + \
              Fore.RED + " to remove.")

    def edit_phone(self, old_phone_str: str, new_phone_str: str):

        new_phone = Phone(new_phone_str)
        if new_phone.is_valid() is False:
            return Fore.RED + "The phone number " + \
                Fore.YELLOW + f"{new_phone}" + \
                Fore.RED + " is not valid."

        # check if there is already new_phone in the record
        # if yes - do nothing

        for phone in self.phones:
            if new_phone_str == phone.value:
                return Fore.RED + "There is already number " + \
                    Fore.YELLOW + f"{new_phone_str}" + \
                    Fore.RED + " in the record. Nothing is edited."
        self.add_phone(new_phone_str)  # if there is no new_phone in the contacts - add it ...

        for phone in self.phones:
            if old_phone_str == phone.value:
                self.remove_phone(old_phone_str)  # ... and delete the old_phone
        return Fore.GREEN + "Number has been edited"

    def find_phone(self, phone: str):
        find_flag = False
        for added_phone in self.phones:  # iterating through list of added objects
            if phone == added_phone.value:  # comparing wanted number with added_object.value
                return True
        if not find_flag:
            return False


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, new_record: Record):
        self.data[new_record.name] = new_record

    def find(self, name: str):
        for contact_name, record in self.data.items():
            if contact_name.value == name:
                return record

    def delete(self, name: str):
        for contact_name in self.data.keys():
            if contact_name.value == name:
                self.data.pop(contact_name)
                break

    def get_birthdays_per_week(self):
        list_of_dicts = []
        for name, record in self.items():
            contacts_dict = {}
            name_str = name.value
            day, month, year = self.data[name].birthday.value.split('.')
            birthday_datetime = datetime(int(year), int(month), int(day))

            contacts_dict["name"] = name_str
            contacts_dict["birthday"] = birthday_datetime

            list_of_dicts.append(contacts_dict)

        return get_birthdays_per_week(list_of_dicts)
