# ineuron_assignment
Screening assignment for ineuron
What is abstract class

```
A class is said to be abstract class if it contains atleast one abstract method(i.e., methods which are defined but has no code in it instead has pass keyword in it.)
Abstract class can be deverived by subclasses and there abstract methods will get defined in subclasses

class Car:
    def __init__(self):
        self.color = Black
    def engineType(self):
        pass

class Tesla(Car):
    def engineType(self):
        print("Electic powered")

class Renault(Car):
    def engineType(self):
        print("Diesel Engine")

class Ford(Car):
    def engineType(self):
        print("Petorl Engine")

t = Tesla()
t.engineType()
r = Renault()
r.engineType()
f = Ford()
f.engineType()


Python has a default class ABC for the use of abstraction in the Python program
from abc import ABC  
class ClassName(ABC): 
```

What is multiple inheritence

```
When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

class Calculation1:   
    def Summation(self,a,b):  
        return a+b;

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b; 

class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20)) 

```

what is decorator in python

```
Decorators are used to add functionality to an existing code without changing it's structure.
In Python, a function is treated as a first-class object. This means that a function has all the rights as  we can assign a function to a variable, pass it to a function or return it from a function. Just like any other variable.

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("before calling func() function")

        a_func()

        print("after calling func function")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

```
