"""
Question 1 (20 points)
1.
A programme is the process of writing instructions that is carried out by a computer. The instructions are written in a
specific programming language also known as code that the computer can understand.
2.
A process usually refers to the start of a programme and is sometimes referred to as a task.
3.
Caches are used to store temporary files, these might be simple files that don't take up much memory but are frequently
used.
4.
A thread is a small set of instructions that are carried out independently and a multithread is multiple sets of
instructions that are carried out at the same time.
5.
GIL is a lock that allows only one a select of code to be exceuted at a time.
6.
cocurrency is when a task is dependannt on another task to run
parralellism - is when a task wrorks idenpendently of other tasks

7.
DRY - dont repeat yourself
KISS - keep it simple
BDUF - big design, up front
8.
a garbage collector is in control of the memory, once a process has been executed the garbage collector moves it to a
secondary sections
9.
a deadstock is when multiple transactions are unwilling to give up its lock
a live stock is when shared locks keep on interrupting each other
10.
flask is a useful feature that has tools that make it easy to build web applications

"""
"""
Question 2 (8 points)
[Your answer]

python 3 is the updated version of python 2 and it is easier to code in and understand in comparison to python 2 
python 3 defult uses unicode where as python 2 does not therefore requires a string to be defined 



"""
"""
Question 3 (8 points)
# Your code here

string = "hannah"

def palindrome(string):

 return string == string[::-1]
print(palindrome(string))

"""
"""
Question 4 (8 points)
"""
"""
import unittest

def is_palindrome_true(self):
    value = Palindrome.is_palindrome('hannah')
    self.aseertequals(value,True)
    




"""
# Your code here
"""
"""
"""
Question 5 (8 points)
planning - these are initial meetings where the developer needs to ask questions so that they fully understand what is 
expected of them and what the client actually wants 

scrum/ sprint meetings - these meetings focus on certain aspects of the programme where they will tackle a small piece 
of the programme to focus on, this usually takes around 2- 4 weeks to develop something and recieve feedback

feedback - because agile is fast paced it requires a lot of feedback meetings, during these meetings the developer will 
gain some insight on what is going well and also areas of potential improvement 

"""
"""
Question 6 (8 points)
[Your answer]

try - lets you test out a piece of code - this is the first step and you only move on to except if this step doesnt work
except - lets you handle a potential error - this lets you catch potential problems in your code 
else - let you continue if there is no error 
finally - lets you execute the code - this should be the last step 




"""
"""
Question 7 (8 points)
[Your answer]
"""
"""
databases can be stored outside of pycharm for example using sql. so the way this works is you store the database 
externally and connect it to your pycharm so that you can work on it. the reason the database is stored externally is to 
prevent the programme being slowed down and to increase efficiency especially if it is a large database. 

so the first step would be to connect python to sql using pip 
In the python terminal you would write a small piece of code to link your sql to your python (this differs
depending on whether or not your using a mac or windows) you would also need to know your username password, host and
the database name. 
then you would import sql connector fill in your personal details and start working on your db, at this stage you should 
be able to write changes in pycharm and it should affect the external database. 
 

"""
"""
"""
"""
Question 8 (10 points)
[Your answer]
"""
"""


SELECT Authors.author_name, Books.sold_copies from Authors 
INNER JOIN Books 
ON Authors.book_name = Books.book_name
ORDER by sold_copies;

"""
"""
Question 9 (22 Points)
"""
"""
# Your code here

def targetSum(randomnum, target):
    result = []
    for x in range(0, len(randomnum) - 1):
        num1 = randomnum[x]
        for y in range(x + 1, len(randomnum)):
            num2 = randomnum[y]
            total = num1 + num2
            if total == target:
                result.append(num1)
                result.append(num2)

    return(result)

print(targetSum([5, 17, 2, 3, 15, 0, -16, 90], 20))



"""