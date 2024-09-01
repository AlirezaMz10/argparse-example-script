# Introduction

Welcome to the argparse-example-script repository! This script demonstrates a simple yet powerful command-line utility written in Python using the argparse library. It allows users to input personal information and formats it into a human-readable sentence.

## What is argparse:

argparse is a module in Python’s standard library used for parsing command-line arguments. It provides a way to handle command-line inputs to your Python scripts, allowing users to specify options and arguments when running the script. This module simplifies the process of writing user-friendly command-line interfaces for Python programs.

```python
import argparse
```

## Features

- Name Input: Accepts a first name using the -n or --name flag.
- Family Name Input: Accepts a family name using the -f or --family flag.
- Age Input: Accepts an age using the -a or --age flag.
- Strict Flag Validation: Only exact flags (-n, --name, -f, --family, -a, --age) are allowed. Abbreviated or unknown flags will result in an error.


## Common Method
- add_argument(name_or_flags, **kwargs): Defines what arguments the program is expecting. name_or_flags can be a string for a positional argument or a list of strings for optional arguments.
```python
parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family.')
parser.add_argument('-a', '--age', type=int, help='Your age.')
```
- parse_args(args=None): Parses the command-line arguments. args can be a list of strings to override default argument parsing.

## Explanation:

1. Abbreviation Disabled:
- allow_abbrev=False ensures that the flags must be used exactly as defined (e.g., --name cannot be abbreviated as --na).

2. Error Handling:
- The script catches SystemExit to handle cases where invalid arguments are provided. This is useful for customizing the error message or further handling invalid inputs.

3. Output Construction:
- The script builds the output string based on which arguments are provided. It checks if name is provided first, then appends family and age as needed.

4. Graceful Fallback:
- If only family or age is provided without name, the script handles these cases separately, ensuring correct output formatting.

## Usage

To use the script, you need to provide the required flags with their corresponding values. Here’s how you can run the script from the command line:

```commandline
python main.py -n <FirstName> -f <FamilyName> -a <Age>
```

### Example

- All Information Provided:
```commandline
python main.py -n Alireza -f Malekzadeh -a 24
```

#### Output:

```commandline
I am Alireza Malekzadeh, I am 24 years old.
```

- Name and Family Only:

```commandline
python main.py -n Alireza -f Malekzadeh
```

#### Output:

```commandline
I am Alireza Malekzadeh
```

- Only name:

```commandline
python main.py -n Alireza
```

#### Output:

```commandline
I am Alireza 
```

- Only Age:

```commandline
python main.py -a 24
```

#### Output:

```commandline
I am 24
```

## Requirements

- Python 3.x
- argparse (included in the Python standard library)

## Refined Script:

```python
import argparse

# Create the argument parser with abbreviation disabled
parser = argparse.ArgumentParser(description='Example script.', allow_abbrev=False)

# Define the command-line arguments
parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family name.')
parser.add_argument('-a', '--age', type=int, help='Your age.')

try:
    # Parse the command-line arguments
    args = parser.parse_args()
except SystemExit:
    # Handle invalid command-line usage
    print("Invalid command")
    exit()

# Initialize the output string
output = ""

# Construct the output based on provided arguments
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

# Print the result
print(output)
```

## Conclusion
argparse is a powerful tool for handling command-line arguments in Python scripts. It simplifies argument parsing, helps manage script inputs, and provides a better user experience by generating help messages and handling errors gracefully.