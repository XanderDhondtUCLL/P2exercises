import re
# Write your code here

def zero_or_more_abc(string):
    return re.fullmatch("(abc)*", string)