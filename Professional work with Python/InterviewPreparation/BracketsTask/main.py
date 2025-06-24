from brackets_function import check_brackets


if __name__ == '__main__':
    brackets = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]

    for i, string in enumerate(brackets):
        print(str(i + 1), check_brackets(string))