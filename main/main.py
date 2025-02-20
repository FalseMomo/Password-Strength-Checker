import strength_checker         

def main():

    password = input('Please enter a password: ')

    check = strength_checker.strength_checker(password)
    print(check)


if __name__ == "__main__":
    main()

    