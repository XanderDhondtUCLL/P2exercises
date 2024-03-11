import re
# Write your code here

def only_digits(string):
    return re.fullmatch("[0123456789]*",string)