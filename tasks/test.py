# # class Shape:
# #     def area(self, *side):
# #         return side[0] * side[1] if len(side) > 1 else (3.14 * side[0]**2)/2
# #
# #
# # class Circle(Shape):
# #     pass
# #
# #
# # class Rectangle(Shape):
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #
# #     def area(self):
# #         return self.width * self.height
# #
# #
# # req = Rectangle(2,4)
# # print(req.area())
# #
# # circle = Circle()
# # print(circle.area(20))
# #
# # shape = Shape()
# # print(shape.area(2))
# #
#
# # class Switchable:
# #     def turn_on(self):
# #         return True
# #
# #     def turn_off(self):
# #         return False
# #
# # class LightBulb(Switchable):
# #     pass
# #
# # class Fan(Switchable):
# #     pass
# #
# # class Switch:
# #     def __init__(self, device):
# #         self.device = device
# #
# #     def operate(self):
# #         if self.device.is_on():
# #             self.device.turn_off()
# #         else:
# #             self.device.turn_on()
# #
# #
# # fan1 = Fan()
# # print(fan1.turn_on())
# # switch_fan1 = Switch(fan1)
# #
# # print(switch_fan1.operate())
#
#
# # version1 = '126.18.15.2b'
# # version2 = '126.18.15.2b'
# #
# # def compare_version(v1, v2):
# #     ver_split1 = v1.split('.')
# #     ver_split2 = v2.split('.')
# #
# #     for ver1, ver2 in zip [ver_split1, ver_split2]:
# #         if ver1.isdigit() and ver2.isdigit():
# #             if ver1 < ver2:
# #                 print(f"{ver1} is less than {ver2}")
# #                 break
# #             elif ver1 > ver2:
# #                 print(f"{ver1} is grater than {ver2}")
# #                 break
# #         elif ver1
#
# class MyContext:
#     def __enter__(self):
#         print("Entering the context")
#         return self  # Can return any object that you want to use within the context
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting the context")
#         # Clean up resources or handle exceptions here
#         if exc_type is not None:
#             print(f"Exception type: {exc_type}")
#             print(f"Exception value: {exc_value}")
#             print("Exception handled!")
#
# # Using the context manager with a 'with' statement
# with MyContext() as my_instance:
#     print("Inside the context")
#     # Uncomment the following line to see exception handling
#     # raise ValueError("An example exception")
#
# # Outside the context
# print("Outside the context")
import math


# def func1(a):
#     yield 123
#     yield 456
#     for el in a:
#         yield el
#
#
# var1 = func1([19, 23])
#
# for el in var1:
#     print(el)
# print(next(var1))
# print(next(var1))


def stars(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percents(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@stars
@percents
def printer(msg):
    print(msg)


printer("Hello!")



class Person:
    __a = "__a"
    b = "b"


    def __init__(self, a):
        self.__value = a
        self.first = "first"


pers_1 = Person(7)

print("=" * 300)

print(vars(Person))
print(vars(pers_1))

print("=" * 300)


print(pers_1._Person__value)
print(pers_1.first)

print("=" * 300)

print(Person._Person__a)
print(Person.b)

print("=" * 300)
print("=" * 300)
print("Creating Classes")


# for t in int, float, dict, list, tuple, Person, pers_1, type:
#     print(type(t))

Class1 = type(
    'Class1',
    (),
    {
        'first': 100,
        'get_first': lambda obj: obj.first + 1
    }
)

x = Class1()
print("From Class1:", x.first, x.get_first())



print("=" * 300)
print("=" * 300)
print("Named tuples")
from collections import namedtuple

Point = namedtuple("Points", "x y z")
print(issubclass(Point, tuple))
point = Point(2, 4, 8)
print(point)
print(point[2])

point = Point(x = 1, y = 3, z = 7)

print(point)
print(point.x, point.z)
print(point[0], point[2])


print("=" * 300)

Person = namedtuple('Person', 'name children')
john = Person('John Doe', ['Timmy', 'Jimmy'])
print(john)
print(id(john.children))

john.children.append('Tina')
print(id(john.children), john.children)


print("=" * 300)
print("=" * 300)
print("Data class")

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    rank: float


st1 = Student("first", "3.2")
st2 = Student("second", "5")
st1.name = 'test'

print(st1, st2)


print("=" * 300)
print("=" * 300)
print("Abstract methods")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 5


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


r = Rectangle(10, 15)
print(r.area())


class Shape3:
    def area(self):
        raise Exception


class Circle(Shape3):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r * self.r * math.pi

s = Circle(5)
print(s.area())


print("=" * 300)
print("=" * 300)
print("deserialization")

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from helpers.file_helpers import *
from typing import List

@dataclass_json
@dataclass
class UserData:
    name: str
    age: int
    city: str
    is_student: bool
    grades: List[int]

def get_users_from_file(file = '../resources/user_data.json'):
    return read_from_file(file, UserData)


print("Deserialized Data:")
print(get_users_from_file())



# # Create a new person and add it to the list
# new_person = UserData(name='Alice', age=28, city='Wonderland', is_student=True, grades=[95, 88, 92])
# user_data.append(new_person)
#
# # Write the updated list of Person objects back to the JSON file
# write_json('people.json', user_data)

print("=" * 300)
print("=" * 300)
print("__str__ and __repr__")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


book_instance = Book("The Python Book", "John Doe")

print(str(book_instance))
print(repr(book_instance))
