from stack import Stack

def check_brackets(string):
    s = Stack()

    bracket_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']

    for element in string:
        if element in open_bracket:
            s.push(element)
        elif element in close_bracket:
            if s.is_empty():
                return False
            else:
                current = s.peek()
                if element != bracket_dict[current]:
                    return False
                else:
                    s.pop()
    return True
