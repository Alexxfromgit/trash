from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):
	"""docstring for GoogleSearch"""
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get('http://google.com')


	def test_01(self):
		driver = self.driver
		driver.find.element_by_id('lst-ib')
		input_field.send_keys('python')
		input_field.send_keys(Keys.ENTER)

		time.sleep(2)

		titles = driver.find.elements_by_class_name('r')
		for title in titles:
			assert "python" in title.text.lower()


	def test_02(self):
		driver = self.driver
		driver.find.element_by_id('lst-ib')
		input_field.send_keys('python')
		time.sleep(1)
		input_field.send_keys(Keys.DOWN)
		input_field.send_keys(Keys.ENTER)

		time.sleep(2)

		titles = driver.find.elements_by_class_name('r')
		for title in titles:
			assert "python" in title.text.lower()


	def tearDown(self):
		self.driver.quit()
		

if __name__ == '__main__':
	unittest.main()

#browser = webdriver.Firefox()
#browser.get('http://google.com')