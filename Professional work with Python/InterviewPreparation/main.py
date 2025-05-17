from symmetry_function import check_symmetry


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
        print(str(i + 1), check_symmetry(string))