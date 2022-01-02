import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


# construct a new parser object
parser = argparse.ArgumentParser(description="This is cipher text decoder CL argument parser.")

# add the rule/acceptable argument
parser.add_argument("--file", help="You need to specify the name of the cipher text input.")

# parse the commandline arguments
args = parser.parse_args()

# given a parsed argument, assign the filename to the a variable
filename = args.file

# open and read the file
opened_file = open(filename)
encoded_text = opened_file.read()

# test print the content of the cipher text input
print(f'This the read text: {encoded_text}')

decode_Caesar_cipher(encoded_text, -13)

# close the file
opened_file.close()
