import pytest


@pytest.fixture()
def before():
    print('\nbefore each test')


def test_1(before):
    print('\ntest_1()')


def test_2(before):
    print('\ntest_2()')


@pytest.mark.usefixtures("before")
def test_3():
    print('test_3()')


@pytest.mark.usefixtures("before")
def test_4():
    print('test_4()')
