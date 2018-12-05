from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_create_user_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("nickname")) > 0):
            wd.find_element_by_link_text("add new").click()


    def create_user(self, contact):
        wd = self.app.wd
        self.open_create_user_page()
        self.fill_form(contact)
        self.submit()
        self.return_to_home_page()
        self.contact_cache = None


    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)


    def select_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not "-":
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_name(field_name).click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]")[index].click()
        self.return_to_home_page()
        self.contact_cache = None


    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)



    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)


    def return_to_home_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("home").click()


    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

