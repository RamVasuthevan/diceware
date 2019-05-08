import sys
import argparse
import pyperclip
from diceware_module import diceware_class

def main():
    password_generator = diceware_class()
    pyperclip.copy(password_generator.create_password())
    print(password_generator.create_password())

if __name__ == '__main__':
    main()
