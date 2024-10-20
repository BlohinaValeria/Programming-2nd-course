'''"""
Creates and returns a function that returns a dictionary with information about a person.
Returns:
function: A function that, when called, returns a dictionary with data about a person.
The dictionary contains the following keys:
'name': The name of the person (string).
- 'surname': The last name of the person (string).
- 'patronymic': The patronymic of the person (string).
- 'birthday': The date of the person's birth (string).
- 'city': The person's city of residence (string).
    """'''

def foo():
    name = 'Valeria'
    surname = 'Blohina'
    patronymic = 'Sergeevna'
    birthday = '10.10.2003'
    city = 'Saint-Petersburg'

    def inner_boo():
        return {'name': name, 'surname': surname, 'patronymic': patronymic, 'birthday': birthday, 'city': city}

    return inner_boo


x = foo()
print(x())
