from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestGitHub:
    def test_Sample1(selft):
        driver=webdriver.chrome("C:\\Users\\sony\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
        driver.get("https://www.google.com/")
        input=driver.find_element_by_name("q")
        input.send_keys('chennai')
        input.send_keys(Keys.ENTER)

    def test_Sample2(self):
        driver = webdriver.chrome("C:\\Users\\sony\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
        driver.get("https://www.bing.com/")
        input = driver.find_element_by_name("q")
        input.send_keys('chennai')
        input.send_keys(Keys.ENTER)
        input=driver.find_element_by_name("qqq")


