from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
         wd = self.wd
         if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get("http://localhost/addressbook/")


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()