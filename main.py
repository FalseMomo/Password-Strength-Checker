import re

def strength_checker(password, filename="Password-Strength-Checker/10-million-password-list-top-1000.txt"):

    """
    This is a program to check the strength of the password based on a set of specified criteria
    """

    with open(filename) as file:

        for line in file:
            word = line.strip()
            if word == password:
                return 'This password has been identified as a common password. Please use a different password!'
                

def main():

    password = input('Please enter a password: ')

    
    print(strength_checker(password))


if __name__ == "__main__":
    main()

    