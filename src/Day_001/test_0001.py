import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ddt import ddt,data,unpack


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://devcas.cre.com.hk/osp-mtmsg-front/#/login'
        cls.driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('msg001')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('msg001')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
        sleep(10)
        self.assertEqual(driver.title, "消息中心-主页")

    def test_query_info(self):
        driver = self.driver
        message_menu = driver.find_element_by_xpath('//*[@id="sidebar"]/div/li[1]/div')
        message_menu.click()
        message_loc = (By.XPATH, '//*[@id="sidebar"]/div/li[1]/ul/a/li')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(message_loc))
        driver.find_element(*message_loc).click()
        sleep(10)


if __name__ == '__main__':
    unittest.main()



