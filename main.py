import argparse

parser = argparse.ArgumentParser(description='Example script.', allow_abbrev=False)

parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family.')
parser.add_argument('-a', '--age', type=int, help='Your age.')

try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid command")
    exit()

output = ""

if args.name:
    output += f"I am {args.name}"
    if args.family:
        output += f" {args.family}"
    if args.age:
        output += f", I am {args.age} years old."
elif args.family:
    output = f"I am {args.family}."
elif args.age:
    output = f"I am {args.age} years old."

print(output)