import pytest
from task_2_my import Library, BookNotFoundError


@pytest.fixture
def moskow_library():
    return Library(['War and Pieac', 'Big russian encyklopedia'])


def test_1(moskow_library):
    moskow_library.add_book('Evgeny Onegin')
    assert moskow_library.list_books() == ['War and Pieac', 'Big russian encyklopedia', 'Evgeny Onegin']


def test_2(moskow_library):
    with pytest.raises(BookNotFoundError):
        moskow_library.remove_book('Evgeny Onegin')


def test_3(moskow_library):
    assert moskow_library.list_books() == ['War and Pieac', 'Big russian encyklopedia']
