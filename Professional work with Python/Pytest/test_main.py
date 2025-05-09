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