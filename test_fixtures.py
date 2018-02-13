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
    
    
"""
import pytest


@pytest.fixture()
def before():
    print('\nbefore each test')


class Test:
    
    def test_1(self, before):
        print('test_class_1()')

    def test_2(self, before):
        print('test_class_2()')
"""





"""
@pytest.fixture(params=[1, 2, 3])
def test_data(request):
    return request.param


# @pytest.mark.skipif(test_data == 2, reason='Because test is failed')
def test_not_2(test_data):
    print('test_data: {}'.format(test_data))
    assert test_data != 2
"""
