import pytest
 
#
# @pytest.fixture()
# def before():
#     print('\nbefore each test')
#
#
# def test_1(before):
#     print('test_1()')
#
#
# def test_2(before):
#     print('test_2()')
#
# # Another way
#
# @pytest.mark.usefixtures("before")
# def test_3():
#     print('test_3()')
#
#
# @pytest.mark.usefixtures("before")
# def test_4():
#     print('test_4()')
#
 
############################################3
 
# class Test:
#     @pytest.mark.usefixtures("before")
#     def test_class_1(self):
#         print('test_class_1()')
#
#     @pytest.mark.usefixtures("before")
#     def test_class_2(self):
#         print('test_class_2()')
#
########################################################3
 
# @pytest.fixture()
# def some_data():
#     data = {'foo': 1, 'bar': 2, 'baz': 3}
#     return data
#
#
# def test_foo(some_data):
#     assert some_data['foo'] == 1
 
 
#########################################################3
 
 
# @pytest.fixture(params=[1, 2, 3])
# def test_data(request):
#     return request.param
#
#
# def test_not_2(test_data):
#     print('test_data: {}'.format(test_data))
#     assert test_data != 2
 
##############################################################3
import getpass
import time
 
 
###################??????????#######################
 
# @pytest.fixture(scope="module", autouse=False)
# def mod_header(request):
#     print('\n-----------------')
#     print('user        : {}'.format(getpass.getuser()))
#     print('module      : {}'.format(request.module.__name__))
#     print('-----------------')
#
#
# @pytest.fixture(scope="function", autouse=False)
# def func_header(request):
#     print('\n-----------------')
#     print('function    : {}'.format(request.function.__name__))
#     print('time        : {}'.format(time.asctime()))
#     print('-----------------')
#
#
# def test_one():
#     print('in test_one()')
#
#
# def test_two():
#     print('in test_two()')
 
###########################  Multiple fixtures #################3
 
 
# @pytest.fixture(scope="module")
# def foo(request):
#     print('\nfoo setup - module fixture')
#
#     def fin():
#         print('foo teardown - module fixture')
#
#     request.addfinalizer(fin)
#
#
# @pytest.fixture()
# def bar(request):
#     print('bar setup - function fixture')
#
#     def fin():
#         print('bar teardown - function fixture')
#
#     request.addfinalizer(fin)
#
#
# @pytest.fixture()
# def baz(request):
#     print('baz setup - function fixture')
#
#     def fin():
#         print('baz teardown - function fixture')
#
#     request.addfinalizer(fin)
#
#
# def test_one(foo, bar, baz):
#     print('in test_one()')
#
#
# def test_two(foo, bar, baz):
#     print('in test_two()')
