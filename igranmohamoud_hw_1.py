"""
TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""
class CashRegister:

    def __init__(self):

        self.items = []
        self.total_items = []
        self.total_price = 0
        self.discount = 0

    def add_item(self, total_items):
        self.item_name += 1
        self.items.append(total_items)

    def remove_item(self,total_items):
        self.item_name -= 1
        self.items.append(total_items)

    def get_total(self):
     print(f'Your total is {self.total_price}')

    def show_items(self):
     print(f'Your total items are {self.total_items}')

    def reset_register(self):

    total_price = []
    total_items = 0

class item:

 def __init__(self, name, price):
    self.item_name = name
    self.item_price = price


Item1 = (item('Ketchup', 3.00))
Item2 =(item('Mayo', 2.50))

CashRegister.add_item(Item1)

print(CashRegister.add_item())
print(CashRegister.get_total())
"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

dict = {"Elle": "software development",
        "Mike":"Data Analyst"}

One = Student('Elle', 17, 2679)
Two = Student('Mike', 17, 3049)


print(f'name: {One.name} - Age: {One.age} years old - ID: {One.id} ')
print(f'name: {Two.name} - Age: {Two.age} years old - ID: {Two.id} ')


class CFGStudent (Student):

    def __init__(self, subjects, grade, students):

        self.subjects = subjects
        self.grade = grade
        self.number_of_students = students
        self.total_subjects = 0

    def add_subject(self, total_subjects):
        self.subjects += 1
        self.subjects.append(total_subjects)
    def remove_subject(self, total_subjects):
        self.subjects -= 1
        self.subjects.append(total_subjects)
    def total_subjects(self, total_subjects):
       return total_subjects
    def overall_mark(self):
        return sum(CFGStudent.grade) / CFGStudent.students


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
