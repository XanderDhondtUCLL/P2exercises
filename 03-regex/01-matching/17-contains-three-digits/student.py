import re
# Write your code here

def contains_three_digits(string):
    return re.fullmatch(".*[0-9].*[0-9].*[0-9]", string)