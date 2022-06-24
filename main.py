# print('hello world.')
# print('testing branch')

# TASK 1


# GIT WORKFLOW FUNDAMENTALS
# Working directoru or working tree, consists of files that you are currently working on, where you can view and modify files.
# The staging area is like a rough draft space, it's where you can git add the version of a file or multiple files that you want to save in your next commit
# The Local repo (HEAD) in Git is the pointer to the current branch reference, which is in turn a pointer to the last commit you made or the last commit that was checked out into your working directory.
# A remote repository in Git, also called a remote, is a Git repository that's hosted on the Internet or another network.


# WORKING DIRECTORY STATES
# A staging step in git allows you to continue making changes to the working directory, and it allows you to record changes in small commits.
# As you edit files, Git sees them as modified, because you've changed them since your last commit.
# The git commit command captures a snapshot of the project's currently staged changes. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicitly ask it to.


# GIT COMMANDS
# The git add command adds a change in the working directory to the staging area
# a commit is an operation which sends the latest changes of the source code to the repository, making these changes part of the head revision of the repository.
# The git push command is used to upload local repository content to a remote repository.
# git fetch is a primary command used to download contents from a remote repository.
# The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch.
# The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content.





# TASK 2 QUESTION 1

user_pin = 1234
user_balance =100



def withdraw_cash():
    while True:
        try:
            withdrawal_amount = int(input("Enter the amount of money you want to withdraw: "))
        except ValueError:
            print("Enter correct amount")
        else:
            if withdrawal_amount > user_balance:
                raise ValueError("You don't have sufficient balance to make this withdrawal")
                is_quit = True
            else:
                remaining_balance = user_balance - withdrawal_amount
                print(f"£{withdrawal_amount} withdrawn from your account, you have {remaining_balance} remaining in your bank.")
        finally:
            print("Program executed")


def main():
    count = 0
    while count < 3:
        try:
            pin = int(input('Please enter your four digit pin: '))
        except ValueError:
            print("Please enter correct pin")
            count += 1
        else:
            if pin != user_pin:
                print("Pin does not match.. Try Again")
                count += 1
            else:
                withdraw_cash()

    if count == 3:
        print('YOU ENTERED THE WRONG PIN 3 TIMES, CARD BLOCKED')
        is_quit = True
    return "thank you, bye"


main()




TASK 3

import unittest
from unittest import TestCase, main
from main import withdraw_cash

class TestWithdrawFunc(TestCase):

    def correct_amount(self):
        expected = 29.50  # withdraw 70.50
        result = withdraw_cash(70.5)
        self.assertEqual(expected, result)

    def test_greater_withdraw(self):
        expected = -10
        result = withdraw_cash(110)
        self.assertEqual(expected,result)

    def test_invalid_data_type(self):
        expected = 100
        result = withdraw_cash('0')
        self.assertEqual(expected, result)

    def test_Withdraw(self):
        withdraw_cash(100)
        self.assertEqual(self.newBalance(-100), 0)

    def test_should_not_allow_negative_balance(self):
        self.remaining.balance()
        self.assertEqual(self.remaining.balance, 0)



if __name__ == '__main__':
    unittest.main()



