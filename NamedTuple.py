from collections import namedtuple

Product = namedtuple('Product', ['name', 'description', 'price', 'quantity'])

smartphone = Product(name = 'iphone 16', description = 'iphone 16', price = 1000, quantity = 5)
lap = Product(name = 'macbook pro', description = 'macbook pro', price = 3000, quantity = 9)

product_data_as_dict = Product._asdict(smartphone)
print(product_data_as_dict)

smarthphone = smartphone._replace(name = 'samsung', price = 600)

print(smarthphone)

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    children: list = ['john', 'ann']

person = Person(name='Test user', age=18)

class Cars(NamedTuple):
    name: str
    color: str
    horsepower: int

bmw = Cars('m8', 'dark blue', 500)

class Student(NamedTuple):
    first_name: str
    last_name: str
    course: int
    age: int

tom = Student('tom', 'dave', 3, 22)


