# save as cli_argparse.py
import argparse

parser = argparse.ArgumentParser(description='Small CLI demo')
subparsers = parser.add_subparsers(dest='command')

greet = subparsers.add_parser('greet')
greet.add_argument('name')

add = subparsers.add_parser('add')
add.add_argument('num1', type=float)
add.add_argument('num2', type=float)

help_parser = subparsers.add_parser('help', help='Show help')

args = parser.parse_args()

if args.command == 'greet':
    print(f'Hello, {args.name}')
elif args.command == 'add':
    print(f'The sum is {args.num1 + args.num2}')
else:
    parser.print_help()
