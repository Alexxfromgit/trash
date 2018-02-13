

from unnecessary_math import multiply


def setup_module(module):
    print("\n\nsetup_module    module:%s" % module.__name__)


def teardown_module(module):
    print("\n\nteardown_module    module:%s" % module.__name__)


class TestUM:
    
    def setup_class(cls):
        print("\n\nsetup_class      class: {}".format(cls.__name__))

    def teardown_class(cls):
        print("\n\nteardown_class         class: {}".format(cls.__name__))

    def setup_method(self, method):
        """the same like def setup class and teardown class"""
        print("\n\nsetup_method     method: {}".format(method.__name__))

    def teardown_method(self, method):
        """the same like def setup class and teardown class"""
        print("\n\nteardown_method     method: {}".format(method.__name__))

    def test_numbers_3_4(self):
        print('\ntest_numbers_3_4 <======================= actual test code')
        assert multiply(3, 4) == 12

    def test_strings_a_3(self):
        print('\ntest_strings_a_2 <======================= actual test code')
        assert multiply('a', 3) == 'aaa'


class TestVM:

    def test_numbers_100(self):
        print('\ntest_numbers_3_4 <======================= actual test code')
        assert multiply(10, 10) == 100

    def test_strings_x_5(self):
        print('\ntest_strings_x_5 <======================= actual test code')
        assert multiply('x', 5) == 'xxxxx'



