import argparse
parser = argparse.ArgumentParser(prog="Jump the five",
                                 description="Encode numbers in a string using 'jump the five' algorithm")
parser.add_argument("string", action="store", help="Input text")

args = parser.parse_args()

dict = {"1": "9", "2": "8", "3": "7", "4": "6", "6": "4", "7": "3", "8": "2", "9": "1", "5": "0", "0": "5"}

strs = list(args.string)
replacement = []

# for s in strs:
#     replacement.append(dict.get(s,s))

letters_out = [dict.get(s, s) for s in strs]

replacement = ''.join(letters_out)

outpt = ""
outpt = outpt.join(replacement)
print(outpt)