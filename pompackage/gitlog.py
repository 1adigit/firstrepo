from selenium import webdriver
from selenium.webdriver.common.by import By


class loggit:

    user_name_id = "login_field"

    user_pass_id = "password"

    user_click = "//input[@type='submit']"

    def __int__(self, driver):
        self.driver = driver

    def enter_user(self,username):
        self.driver.find_element(By.ID,"user_name_id").send_keys(username)


    def enter_pass(self,password):
        self.driver.find_element(By.ID,"user_pass_id").send_keys(password)

    def clicks(self):
        self.driver.find_element(By.XPATH,"user_click").click()





