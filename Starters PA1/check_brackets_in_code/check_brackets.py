# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = (sys.stdin.read()).strip() # get rid off the '\n' if enters from input
    
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket
            opening_brackets_stack.append((i+1,next))
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket
            if opening_brackets_stack == []: # if there is no opening bracket
                opening_brackets_stack.append((i+1,next))
                break
            elif opening_brackets_stack != []:
                bracket_i = Bracket(opening_brackets_stack[-1][1], i) 
                if bracket_i.Match(next) == False:
                    opening_brackets_stack = []
                    opening_brackets_stack.append((i+1,next))
                    break
                else:
                    opening_brackets_stack.pop()
    # Printing answer
    if opening_brackets_stack == []:
        print('Success')
    else:
        print(opening_brackets_stack[0][0])

    
