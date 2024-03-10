import re
# Write your code here

def three_to_ten_times_abc(string):
    return re.fullmatch("(abc){3,10}",string)