import sys
import argparse
import pyperclip
from diceware_module import diceware_class

def main():
    password_generator = diceware_class()
    pyperclip.copy('The text to be copied to the clipboard.')
    print(password_generator.create_password())

if __name__ == '__main__':
    main()
