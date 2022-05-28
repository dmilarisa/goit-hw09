def input_error(func):
    def wrapper(*args):
        try:
            value = func(*args)
            return value
        except (KeyError, ValueError, IndexError):
            return False
    return wrapper

dict_contacts = {}

@input_error
def add_handling(string):
    string = string.strip()
    name, phone = string.split()[0], string.split()[1]
    dict_contacts[name] = phone


@input_error
def change_handling(string):
    string = string.strip()
    name, phone = string.split()[0], string.split()[1]
    if name in dict_contacts.keys():
        dict_contacts[name] = phone
    else:
        raise KeyError


@input_error
def phone_handling(string):
    string = string.strip()
    return dict_contacts[string]