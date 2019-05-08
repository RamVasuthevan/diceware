import argparse
from diceware_module import diceware_class


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", metavar="formater code",
                    type=str, nargs=1, help="ADD HELP FOR -f")
parser.add_argument("-n", "--numbers", metavar="Vaild numbers",
                    type=str, nargs=1, help="ADD HELP FOR -n")
parser.add_argument("-s", "--special", metavar="Vaild special characters",
                    type=str, nargs=1, help="ADD HELP FOR -s")
args = parser.parse_args()

format = None
spec_char= None
numbers=None

if args.format is not None:
    format = args.format[0]

if args.special is not None:
    spec_char = args.special[0]

if args.numbers is not None:
    numbers = args.numbers[0]

diceware = diceware_class(format=format,numbers=numbers,spec_char=spec_char)

print(diceware.create_password())
