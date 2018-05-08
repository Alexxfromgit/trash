from selenium.webdriver.common.keys import Keys
from core.conditions import empty, text, css_class
from core.tools import visit, s
from base_test import *


class TestTodoMVC(BaseTest):
	"""
	docstring for TestTodoMVC
	end-to-end tests
	"""
	def test_tasks_life_cycle(self):
		visit("http://todomvc.com/examples/troopjs_require/#/")

		s("#new-todo").send_keys("a" + Keys.ENTER)

		ss("#todo-list>li").find(text, "a").s("label").double_click()


