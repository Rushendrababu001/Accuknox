''' Topic: Custom Classes in Python
Description: You are tasked with creating a Rectangle class with the following requirements:

The Rectangle class stores attributes like length and width in a list.
The __iter__() method uses Python’s iter() to return an iterator over that list.
Python handles stopping the iteration automatically using StopIteration.'''

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

rect = Rectangle(10, 20)

for attribute in rect:
    print(attribute)
