# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class test_first(unittest.TestCase):

     def setUp(self):
         self.wd = webdriver.Chrome()
         self.wd.implicitly_wait(30)

     def test_first(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups(wd)
        self.fill_group_form(wd, Group(name="test", header="test", footer="test1"))
        self.submit(wd)
        self.open_groups(wd)
        self.logout(wd)

     def test_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups(wd)
        self.fill_group_form(wd, Group(name="", header="", footer=""))
        self.submit(wd)
        self.open_groups(wd)
        self.logout(wd)

     def logout(self, wd):
         wd.find_element_by_link_text("Logout").click()


     def open_groups(self, wd):
         wd.find_element_by_link_text("groups").click()


     def submit(self, wd):
         wd.find_element_by_name("submit").click()


     def fill_group_form(self, wd, group):
         wd.find_element_by_name("new").click()
         wd.find_element_by_name("group_name").click()
         wd.find_element_by_name("group_name").clear()
         wd.find_element_by_name("group_name").send_keys(group.name)
         wd.find_element_by_name("group_header").click()
         wd.find_element_by_name("group_header").clear()
         wd.find_element_by_name("group_header").send_keys(group.header)
         wd.find_element_by_name("group_footer").click()
         wd.find_element_by_name("group_footer").clear()
         wd.find_element_by_name("group_footer").send_keys(group.footer)


     def login(self, wd, username, password):
         wd.find_element_by_name("user").click()
         wd.find_element_by_name("user").clear()
         wd.find_element_by_name("user").send_keys(username)
         wd.find_element_by_xpath("//form[@id='LoginForm']/label[2]").click()
         wd.find_element_by_name("pass").click()
         wd.find_element_by_name("pass").clear()
         wd.find_element_by_name("pass").send_keys(password)
         wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


     def open_home_page(self, wd):
         wd.get("http://localhost/addressbook/")




     def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
     def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
     def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()