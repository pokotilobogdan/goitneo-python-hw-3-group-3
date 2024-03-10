from CLI import Phone
from CLI import Birthday
from colorama import Fore


class WrongInputOrder(Exception):
    pass


class WrongShowInputOrder(Exception):
    pass


class WrongInputNumber(Exception):
    pass


class WrongBirthdayInput(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        text_arguments_list = args[0]
        try:
            if len(text_arguments_list) != 2:
                raise WrongInputNumber
            name_str, phone_str = text_arguments_list
            if name_str.isalpha() is False or Phone(phone_str).is_valid() is False:
                raise WrongInputOrder
            return func(*args, **kwargs)
        except WrongInputOrder:
            return Fore.RED + "Type name first and then valid phone"
        except WrongInputNumber:
            return Fore.RED + "Wrong number of inputs. 2 is required"
        except:
            return Fore.RED + "This is some other error in input_error"

    return inner


def change_error(func):
    def inner(*args, **kwargs):
        text_arguments_list = args[0]
        try:
            if len(text_arguments_list) != 3:
                raise WrongInputNumber
            if text_arguments_list[0].isalpha() is False or text_arguments_list[1].isdigit() is False:
                raise WrongInputOrder
            return func(*args, **kwargs)
        except WrongInputOrder:
            return Fore.RED + "Type name first and then phones"
        except WrongInputNumber:
            return Fore.RED + "Wrong number of inputs. 3 is required"
        except:
            return Fore.RED + "This is some other error in change_error"

    return inner


def birthday_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) != 2:
                raise WrongInputNumber
            name_str, birthday_str = args[0]
            if name_str.isalpha() is False or birthday_str.isalpha() is True:
                raise WrongInputOrder
            if Birthday(birthday_str).isvalid() is False:
                raise WrongBirthdayInput
            return func(*args, **kwargs)
        except WrongInputOrder:
            return Fore.RED + "Type name first and birthday second"
        except WrongInputNumber:
            return Fore.RED + "Wrong number of inputs. 2 is required"
        except WrongBirthdayInput:
            return Fore.RED + "Use DD.MM.YYYY format"
        except:
            return Fore.RED + "This is some other error in birthday_error"

    return inner


def show_error(func):
    def inner(*args, **kwargs):
        text_arguments_list = args[0]
        try:
            if len(text_arguments_list) != 1:
                raise WrongInputNumber
            if text_arguments_list[0].isalpha() is False:
                raise WrongShowInputOrder
            return func(*args, **kwargs)
        except WrongShowInputOrder:
            return Fore.RED + "Type name after the 'phone' command"
        except WrongInputNumber:
            return Fore.RED + "Wrong number of inputs. 1 is required"
        except:
            return Fore.RED + "This is some other error in show_error"

    return inner
