import sys
from diceware_module import diceware_class


def main():
    password_generator = diceware_class()
    #print(password_generator.create_password())
    print(password_generator.create_password())


if __name__ == '__main__':
    main()
