CLI Password Generator

Overview:-
This is a simple Python command-line application that generates strong, secure passwords composed of letters, digits, and special characters.

Features:-
-Adjustable password length based on user input

-Supports uppercase and lowercase letters

-Includes numerical digits

-Incorporates special symbols for added complexity

-Randomizes character order to enhance security

Installation:-
-Ensure Python 3.x is installed on your system.

-Clone this repository to your local machine by running:

Input the desired count of letters, numbers, and symbols for your password.

The program will generate and present a randomized password according to your specifications.

Example Session:

Welcome to the password generator
Enter the number of letters for your password: 5
Enter the number of digits for your password: 3
Enter the number of special characters for your password: 2
Here is your generated password: gT9!a2B#x

Sample Code
python
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*'

def generate_password():
    print("Welcome to the password generator")
    n_letters = int(input("Enter the number of letters for your password: "))
    n_numbers = int(input("Enter the number of digits for your password: "))
    n_symbols = int(input("Enter the number of special characters for your password: "))

  
generate_password()

Author - Avinash Dubey
