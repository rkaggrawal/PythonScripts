import argparse
# help(argparse)

parser = argparse.ArgumentParser(description="displays square")

# positional argument
parser.add_argument("num", type=int, help="please pass integer type number.")

# optional argument with default value
parser.add_argument("--name",help="this  is optional", default='Raj')

# store all arguments in args
args = parser.parse_args()

# calculate square
result = args.num**2

# print values
print('This program is being executed by {} '.format(args.name))
print("Square value of {} is {}".format(args.num, result), end='')