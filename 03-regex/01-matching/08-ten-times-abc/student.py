import re
# Write your code here

def ten_times_abc(string):
    return re.fullmatch("(abc){10}", string)