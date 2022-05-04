import math

# all simple objects
int_test = 7
float_test = 6.23
str_test = "microwave"
bool_test = True

# list/tuple
list_test = ['one', 2, 'three']
tuple_test = tuple(list_test)

# dict
dict_test = {
    "id": 101,
    "company": "GeeksForGeeks",
    "topics": {"Data Structure",
               "Algorithm",
               "Gate Topics"},
    "speed": ("clock", 100),
    "modules": ["numpy", "simpy", "math"]
}


class TestClass:
    def __init__(self):
        self.el1 = 't'
        self.el2 = 2


# function test suite

# global variable
age = 'eighteen'


# function with globals variable
def question():
    global age
    return 'How old are you? Age:' + age


# function with parameters
def mul_params(a, b):
    return a * b

# Bytoma function
c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)
