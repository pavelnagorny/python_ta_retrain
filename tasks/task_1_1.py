from helpers.custom_exceptions import *


class Answer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def answer(self):
        print(f'HELLO, {self.name}')
        print(f'YOUR AGE IS {self.age}')
        print(f'YOU LIVE IN {self.city}')


name = input('WHAT IS YOUR NAME? ')
if name[0].islower():
    raise StartsWithLowerCaseError('name')
elif len(name) < 2:
    raise ShortInputException('name', length=len(name), at_least=2)
age = int(input('HOW OLD ARE YOU? '))
if age < 1 or age > 99:
    raise InvalidAgeException('age', 1, 99)
city = input('WHERE DO YOU LIVE? ')
if city[0].islower():
    raise StartsWithLowerCaseError('city')
elif len(name) < 2:
    raise ShortInputException('name', length=len(name), at_least=2)

# Create an instance of the Answer class
member = Answer(name, age, city)

# Call the answer method
member.answer()
