import unittest
import HtmlTestRunner
from selenium import webdriver
import time

import sys
sys.path.append("E:/PyCharm/BS23_Automation(Python_Unittest_POM)")
from pageObjects.homepage import HomePage
from pageObjects.signin_page import SigninPage
from pageObjects.register_page import RegisterPage


class RegisterTest(unittest.TestCase):

    baseurl = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(
        executable_path="E:\\PyCharm\\BS23_Automation(Python_Unittest_POM)\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()
        time.sleep(3)

    def test_register(self):
        hp = HomePage(self.driver)
        lp = SigninPage(self.driver)
        rp = RegisterPage(self.driver)

        hp.login_Click()
        time.sleep(3)

        lp.setNewEmail("palashdx007@gmail.com")
        lp.ClickEmailCheck()
        time.sleep(3)

        rp.setGender()
        time.sleep(2)

        rp.setFname("Shahidul")
        rp.setLname("Islam")
        rp.setPassword("102030")

        rp.setDob_days('23')
        time.sleep(3)

        rp.setDob_Months('7')
        time.sleep(3)

        rp.setDob_years('1994')
        time.sleep(3)

        rp.setAddress("12,Sovro Street")
        time.sleep(1)

        rp.setCity("Homor")
        time.sleep(3)

        rp.setState('2')
        time.sleep(3)

        rp.setPostcode('11000')
        rp.setCountry('1')
        time.sleep(1)

        rp.setMobile('01810066496')
        time.sleep(1)
        rp.setAlias("Alias Address")
        time.sleep(1)

        rp.setRegisterBtn()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed......")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\\PyCharm\\BS23_Automation(Python_Unittest_POM)\\reports"))