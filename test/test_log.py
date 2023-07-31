from selenium import  webdriver
from pompackage.gitlog import loggit

class test_git:
    baseurl = "https://github.com/login"
    useremail = "adijadhav021997@gmail.com"
    userpass = "github@2157"

    def test_page(self):
        self.driver = webdriver.edge
        self.g = loggit(self.driver)
        self.g.enter_user(self.useremail)
        self.g.enter_pass(self.userpass)
        self.g.clicks()