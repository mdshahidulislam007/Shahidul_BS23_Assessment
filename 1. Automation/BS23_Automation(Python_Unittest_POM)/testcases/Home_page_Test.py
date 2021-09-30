import unittest
import HtmlTestRunner
from selenium import webdriver
import time

import sys
sys.path.append("E:/PyCharm/BS23_Automation(Python_Unittest_POM)")
from pageObjects.homepage import HomePage

class HomePageTest(unittest.TestCase):
    baseurl = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="E:\\PyCharm\\BS23_Automation(Python_Unittest_POM)\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()
        time.sleep(3)

    def test_HomepageTitle(self):
        self.driver.get(self.baseurl)
        print(self.driver.title)
        self.assertEqual("My Store",self.driver.title,"Webpage title is not matching!!!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed......")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\\PyCharm\\BS23_Automation(Python_Unittest_POM)\\reports"))

