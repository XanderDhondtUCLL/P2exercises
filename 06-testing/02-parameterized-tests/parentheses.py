def matching_parentheses(string):
    if string != '':
        if string[0] == ')' or string[::-1] == '(':
            return False
        
    
    count = 0
    for char in string:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
    return count == 0
