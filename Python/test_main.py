import pytest

from main import pluralize_bottles
from main import verse


TEST_PLURALS = [
    (0, "s"),
    (1, ""),
    (2, "s"),
    (11, "s"),
    (20, "s"),
    (55, "s"),
]

TEST_VERSES = [
    (1, "1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\n"),
    (2, "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n\n"),
    (11, "11 bottles of beer on the wall, 11 bottles of beer.\nTake one down and pass it around, 10 bottles of beer on the wall.\n\n"),
    (20, "20 bottles of beer on the wall, 20 bottles of beer.\nTake one down and pass it around, 19 bottles of beer on the wall.\n\n"),
    (55, "55 bottles of beer on the wall, 55 bottles of beer.\nTake one down and pass it around, 54 bottles of beer on the wall.\n\n"),
]


@pytest.mark.parametrize("count, expected", TEST_PLURALS)
def test_pluralize_bottles(count: int, expected: str):
    assert expected == pluralize_bottles(count)


@pytest.mark.parametrize("count, expected", TEST_VERSES)
def test_verse(count: int, expected: str):
    assert expected == verse(count)
