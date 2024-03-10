import re
# Write your code here

def abc_or_xyz(string):
    return re.fullmatch("(abc)|(xyz)", string)