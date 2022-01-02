import sys

args = sys.argv
print(args)

if len(args) == 5:
    args = [int(x) for x in args[1::]]
    print(sum(args))

