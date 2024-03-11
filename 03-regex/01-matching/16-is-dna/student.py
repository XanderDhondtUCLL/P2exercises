import re
# Write your code here

def is_dna(string):
    return re.fullmatch("[ACGT]*", string)