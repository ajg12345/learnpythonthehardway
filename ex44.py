#inheritance vs composition
#Zed Shaw believes that inheritance can be simplified or replaced with womposition, and multiple inheritance should be avoided at all costs

#with inheritance, there are three ways that the parent adn child classes can interact:
"""
1. Actions on the child imply an action on the parent.
2. Actions on the child override the action on the parent.
3. Actions on the child alter the action on the parent.
"""

#examples for case 1:
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass
dad = Parent()
son = Child()

dad.implicit()
son.implicit()


#examples for case 2:
class Parent2(object):
    def override(self):
        print("PARENT override()")

class Child2(Parent2):
    def override(self):
        print("CHILD override()")

dad = Parent2()
son = Child2()

dad.override()
son.override()

#examples for case 3:
class Parent3(object):
    def altered(self):
        print("PARENT altered()")

class Child3(Parent3):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child3, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent3()
son = Child3()

dad.altered()
son.altered()

"""
So thats inheritance (except for multiple inheritance, which is tricky because of MRO, method resolution order)
"""
#Here is Composition, where instead of writing new code to replace or alter functionality (in 2/3 of cases), 
#   we just functions in a module. Here's an example

class Other5(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")

class Child5(object):
    def __init__(self):
        self.other = Other5()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child5()

son.implicit()
son.override()
son.altered()
# so in this case the Child5 has-a Other5 object, but not is-a Other5 object.

#ultimately inheritance versus composition comes down to an attemp to solve the problem of reusable code
"""
Takeaways:
1. avoid multiple inheritance
2. Use composition to package code into modules, used in many different places and situations
3. Use inheritance only when ther are clearly related reusable pieces of code that fit under a single common concept, or if required"""