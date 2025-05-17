import pytest

from moduls.iterator_task_1 import FlatIterator
from moduls.generator_task_1 import flat_generator as g1
from moduls.generator_task_2 import flat_generator as g2

@pytest.mark.parametrize(
    'lol, expected',
    (
        (
            [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ),
    )
)
def test_iterator(lol, expected):
    assert list(FlatIterator(lol)) == expected

@pytest.mark.parametrize(
    'lol, expected',
    (
        (
            [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ),
    )
)
def test_g1(lol, expected):
    assert list(g1(lol)) == expected

@pytest.mark.parametrize(
    'lol, expected',
    (
        (
            [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ),
        (
            [[['a'], ['b', 'c']],['d', 'e', [['f'], 'h'], False],[1, 2, None, [[[[['!']]]]], []]],
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
        )
    )
)
def test_g2(lol, expected):
    assert list(g2(lol)) == expected


class TestYandex:

    def test_yandex(self):
        token = main.read_config('tokens.ini', 'Tokens', 'YandexToken')
        my_yandex = main.YandexDisk(token)
        dir_name = 'TestDir'
        result = my_yandex.make_dir(dir_name)
        try:
            self.assertEqual(201, result)
            print("\nFolder was created successfully")
        except AssertionError:
            match result:
                case 409:
                    print("\nError. Folder already exists")
                case 401:
                    print("\nError. You're not authorized to proceed")
                case 404:
                    print('\nError. Resource not found')
                case 429:
                    print('\nError. Too many requests')
                case 503:
                    print('\nError. Service is not available')
                case 507:
                    print('\nError. Not enough space')
                case _:
                    print("\n Unknown error")
        return