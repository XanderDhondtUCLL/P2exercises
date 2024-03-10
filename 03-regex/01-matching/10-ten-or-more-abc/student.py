import re

# Write your code here
def ten_or_more_abc(string):
    return re.fullmatch("(abc){10,}", string)