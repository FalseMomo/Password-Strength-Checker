import re

def strength_checker(password, filename="Password-Strength-Checker/10-million-password-list-top-1000.txt"):

    """
    This is a program to check the strength of the password based on a set of specified criteria
    """

    # parses a common passwords text file to check if the given password is a common password
    with open(filename) as file:

        for line in file:
            word = line.strip()
            if word == password:
                return 'This password has been identified as a common password. Please use a different password!'
            
    # checks if the length of the password is at least 16 characters long (according to cisa.gov)
    if len(password) < 16:
        return 'This password must be at least 16 characters long. Please use a different password!'
    
    # checks if there is at least 1 uppercase letter in the password (according to cisa.gov)
    if not re.findall('[A-Z]+', password):
        return 'This password must contain at least one uppercase letter. Please use a different password!'
    
    if not re.findall('[0-9]+', password):
        return 'This password must contain at least one digit. Please use a different password!'
    
    if not re.findall('[!@$%^&*+#;:<>?,.~`]+', password):
        return 'This password must contain at least one special character. Please use a different password!'
    
    return 'This password is strong.'
                

def main():

    password = input('Please enter a password: ')

    check = strength_checker(password)
    print(check)


if __name__ == "__main__":
    main()

    