import re

def strength_checker(password, filename="Password-Strength-Checker/10-million-password-list-top-1000.txt"):

    """
    This is a program to check the strength of the password based on a set of specified criteria
    """

    checker = False

    # parses a common passwords text file to check if the given password is a common password
    try:
        with open(filename) as file:
            word_set = set() # uses a set for faster access to words
            for line in file:
                word = line.strip()
                word_set.add(word)
        
        if password in word_set:
            print ('This password has been identified as a common password. Please use a different password!')
            checker = True

        lower_password = password.lower()
        common_password_notifier = False
        for word in word_set:
            if word in lower_password:
                common_password_notifier = True

    # handles FileNotFound error                
    except FileNotFoundError:
        print ("Cannot find the common passwords text file!")
        checker = True
            
    # checks if the length of the password is at least 16 characters long (according to cisa.gov)
    if len(password) < 16:
        print ('This password must be at least 16 characters long. Please use a different password!')
        checker = True
    
    # checks if there is at least 1 uppercase letter in the password (according to cisa.gov)
    if not re.findall('[A-Z]+', password):
        print ('This password must contain at least one uppercase letter. Please use a different password!')
        checker = True
    
    # checks if there is at least 1 digit in the password (according to cisa.gov)
    if not re.findall('[0-9]+', password):
        print ('This password must contain at least one digit. Please use a different password!')
        checker = True
    
    # checks if there is at least 1 special character in the password (according to cisa.gov)
    if not re.findall('[!@$%^&*+#;:<>?,.~`("\')-_={/}[]|\\]+', password):
        print ('This password must contain at least one special character. Please use a different password!')
        checker = True
    
    # checks if the requirements for a strong password have been met
    if (not checker):
        # checks if the password has a common password inside of it
        if (common_password_notifier):
            return 'This password passes all of the basic requirements for a strong password.' + \
            ' Just be aware that the program detected a common password somewhere in your password!'
        else: 
            return 'This password passes all of the basic requirements for a strong password.'
    else: 
        return 'Your password is not strong enough. Please consider modifying it or using a different password!'
                