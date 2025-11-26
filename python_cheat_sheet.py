"""
Python Cheat Sheet
==================

This is a comprehensive Python reference covering the most important concepts and syntax.
"""

# 1. VARIABLES AND DATA TYPES
# ==========================

# Numbers
integer = 42
floating_point = 3.14
complex_num = 3 + 4j

# Strings
string1 = "Hello"
string2 = 'World'
multiline = """This is a
multiline string"""

# Booleans
boolean_true = True
boolean_false = False

# None type
none_value = None

# 2. COLLECTIONS
# ==============

# Lists - ordered, mutable, allows duplicates
my_list = [1, 2, 3, "apple", 3.14]
my_list.append(42)
my_list.remove("apple")
first_item = my_list[0]

# Tuples - ordered, immutable, allows duplicates
my_tuple = (1, 2, 3, "banana")
single_item_tuple = (42,)  # Note the comma

# Dictionaries - key-value pairs, unordered (Python < 3.7) or ordered (Python >= 3.7)
my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
name = my_dict["name"]
age = my_dict.get("age")  # Safe way with default None

# Sets - unordered, mutable, no duplicates
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.discard(1)  # Remove if exists, no error if doesn't

# 3. CONTROL FLOW
# ===============

# Conditionals
if boolean_true:
    print("This is true")
elif boolean_false:
    print("This won't run")
else:
    print("Else case")

# For loops
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for item in my_list:
    print(item)

for key, value in my_dict.items():
    print(f"{key}: {value}")

# While loops
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# 4. FUNCTIONS
# ============

def my_function(param1, param2="default"):
    """
    Function with required and optional parameters
    """
    return param1 + " " + param2

result = my_function("Hello", "World")

# Lambda functions
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# 5. LIST COMPREHENSIONS
# ======================

# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# With condition and transformation
processed = [x**2 if x % 2 == 0 else x**3 for x in range(10)]

# 6. EXCEPTION HANDLING
# =====================

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"General error: {e}")
else:
    print("No exception occurred")
finally:
    print("This runs regardless of exceptions")

# 7. CLASSES AND OBJECTS
# ======================

class MyClass:
    class_variable = "shared by all instances"
    
    def __init__(self, value):
        self.instance_variable = value
    
    def my_method(self):
        return f"Value is {self.instance_variable}"
    
    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_variable}"
    
    @staticmethod
    def static_method():
        return "Static method called"

obj = MyClass("Hello")
print(obj.my_method())

# 8. FILE OPERATIONS
# ==================

# Reading a file
# with open('file.txt', 'r') as f:
#     content = f.read()
#     lines = f.readlines()

# Writing to a file
# with open('file.txt', 'w') as f:
#     f.write("Hello, World!")

# 9. STRING OPERATIONS
# ====================

text = "Hello, World!"
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.split(", "))
print(" ".join(["Hello", "Python", "World"]))
print(f"Formatted string: {text}")

# 10. USEFUL BUILT-IN FUNCTIONS
# =============================

numbers = [1, 2, 3, 4, 5]
print(len(my_list))          # Length
print(max(numbers))          # Maximum
print(min(numbers))          # Minimum
print(sum(numbers))          # Sum
print(sorted(numbers))       # Returns new sorted list
print(any([False, True]))    # True if any element is True
print(all([True, True]))     # True if all elements are True
print(enumerate(["a", "b"])) # Index-value pairs
print(zip([1, 2], ["a", "b"])) # Pairs from multiple iterables

# 11. IMPORTS
# ===========

# import module
# from module import function
# from module import function as alias
# import module as alias

# 12. COMMON MODULES
# ==================

# import os           # Operating system interface
# import sys          # System-specific parameters and functions
# import math         # Mathematical functions
# import datetime     # Date and time handling
# import json         # JSON encoder and decoder
# import re           # Regular expressions
# import random       # Random number generation
# import collections  # Additional data structures
# import itertools    # Efficient looping tools

# 13. DATE AND TIME
# =================

from datetime import datetime, date, time
now = datetime.now()
today = date.today()
specific_time = time(14, 30, 0)

# 14. REGULAR EXPRESSIONS
# =======================

import re
pattern = r"\d+"  # Match one or more digits
text = "There are 123 apples"
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")

# 15. LIST AND DICTIONARY METHODS
# ===============================

# List methods
my_list = [1, 2, 3, 2, 4]
print(my_list.count(2))      # Count occurrences
print(my_list.index(3))      # Find index of first occurrence
my_list.sort()               # Sort in place
my_list.reverse()            # Reverse in place

# Dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# 16. SET OPERATIONS
# ==================

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))          # {1, 2, 3, 4, 5}
print(set1.intersection(set2))   # {3}
print(set1.difference(set2))     # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# 17. DECORATORS
# ==============

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# 18. GENERATORS
# ==============

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# Generator expression
gen_expr = (x**2 for x in range(5))

# 19. CONTEXT MANAGERS
# ====================

class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContextManager() as cm:
    print("Inside context")

# 20. TYPE HINTS (Python 3.5+)
# ============================

from typing import List, Dict, Optional

def typed_function(name: str, age: int) -> str:
    return f"{name} is {age} years old"

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def optional_param(value: Optional[str] = None) -> str:
    return value or "default"

# Print examples
if __name__ == "__main__":
    print("Python Cheat Sheet Examples:")
    print("-" * 30)
    
    # Test basic operations
    print(f"2 + 2 = {2 + 2}")
    print(f"List: {my_list}")
    print(f"Dictionary: {my_dict}")
    print(f"Square of 5: {square(5)}")
    print(f"Current date and time: {datetime.now()}")
    
    say_hello("Python Learner")