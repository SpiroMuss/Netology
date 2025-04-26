class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        self.new_list = []

        if self.cursor == len(self.list):
            raise StopIteration

        if type(self.list[self.cursor]) is list:
            for item in list(FlatIterator(self.list[self.cursor])):
                for i in item:
                    self.new_list.append(i)

        else:
            self.new_list.append(self.list[self.cursor])

        return self.new_list


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    list_of_lists_2 = [[['a'], ['b', 'c']], ['d', 'e', [['f'], 'h'], False], [1, 2, None, [[[[['!']]]]], []]]
    print(list(FlatIterator(list_of_lists_2)))

    # Это мой лучший результат. Я примерно понимаю почему остаются первые листы, но вообще без идей как от них избавиться...
